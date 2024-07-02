import React from 'react';

import CloseIcon from '@mui/icons-material/Close';

import { Box, Button } from "@mui/material";
import { TabsContext } from './TabsContext'; // Importe seu contexto de abas

class TabBar extends React.Component {
   static contextType = TabsContext


   render() {
      const { tabs, switchTab, closeTab, activeTab } = this.context
      return (
         <Box
            sx={{
               display: 'flex',
               maxWidth: '100%',
               gap: 1,
               margin: '30px 0 0 20px',
               overflowX: 'auto',
               objectFit: 'contain',
               whiteSpace: 'nowrap',
               '& > *': { // Coloca estilo em cada item dentro do contêiner
                  flexShrink: 0, // Não deixa os itens encolherem
                  marginRight: '8px',
               },

               // estilização scroll-bar - CHROME
               '&::-webkit-scrollbar-thumb': {
                  backgroundColor: this.props.colors.blueAccent[300],
                  borderRadius: '10px',
               },
               '&::-webkit-scrollbar-track': {
                  background: this.props.colors.custom['colorWhite']
               },
               '&::-webkit-scrollbar': {
                  height: '10px',
                  marginTop: '10px',
               },
            }}
         >
            {tabs.map(tab => (
               <Box
                  sx={[
                     {
                        position: 'relative',
                        borderTop: '3px solid transparent',
                        borderRadius: '0',
                        marginBottom: '5px',
                        ":hover": { borderRadius: '0', borderTop: `3px solid ${this.props.colors.blueAccent[300]}`, },
                     },
                     activeTab === tab.key && {
                        border: `2.5px solid ${this.props.colors.blueAccent[300]}`,
                        borderBottom: 'none',
                        borderRadius: '7px 7px 0 0',
                        ":hover": { borderRadius: '7px 7px 0 0', borderTop: `2.5px solid ${this.props.colors.blueAccent[300]}`, },
                     }
                  ]}
               >
                  <Button
                     sx={{ paddingRight: '30px', width: '100%', fontWeight: '600', letterSpacing: '1px', ":hover": { backgroundColor: 'transparent' } }}
                     key={tab.key}
                     onClick={() => {
                        switchTab(tab.key)
                        this.props.switchTab(tab.key)
                     }}
                  >
                     {tab.title}
                  </Button>

                  <CloseIcon onClick={() => closeTab(tab.key)} sx={{ position: 'absolute', right: '5px', top: '5px', cursor: 'pointer' }} />
               </Box>
            ))}
         </Box>
      )
   }
}

export default TabBar