import React from "react";
import ReactDOM from "react-dom";

import dayjs from 'dayjs';
import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainDateTimeInput from "../../components/inputs/MainDateTimeInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class PortalMessage extends React.Component {
   constructor(props) {
      super(props)
      this.state = {
         isLoading: true,
         isLoadingTab: true,
         isLoadingPortalMessageTable: true,

         menuId: '32',

         search: '',
         isCurrent: false,
         isExpired: false,
         messageCode: '',
         isANewPortalMessage: false,

         portalMessage: {},
         portalMessageList: [],
         portalMessageColumns: {},
         portalMessageTotalSize: '',

         tabs: [
            { id: 'data', title: 'Mensagem' },
         ],
      }
   }

   closeEditTab = () => {
      var element = document.getElementById('edit-tab')
      element.parentNode.removeChild(element)
      this.onPortalMessageTableChange(0)
   }

   componentDidMount() {
      addLastAccess(this.state.menuId)
      this.onPortalMessageTableChange(0)
   }

   createEditTab = (params, isRegister = false) => {
      if (isRegister) {
         this.setState({
            selectedRow: params,
            isLoadingTab: true,
            activeTab: 'data',
            portalMessage: {
               datainicial: dayjs(),
               datafinal: dayjs(),
               vendedor: false,
               varejo: false,
               clienteb2b: false,
               clienteb2c: false,
               representante: false,
            }
         }, () => createEditTab('Mensagens do Portal de Vendas', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
      } else {
         this.setState({
            isANewPortalMessage: false,
            selectedRow: params,
            isLoadingTab: true,
         }, () => createEditTab('Mensagens do Portal de Vendas', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
      }
   }

   handleChangeTab = (event) => {
      if (this.state.isLoadingTab && !this.state.isANewPortalMessage) {
         ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchPortalMessageInfo())
         return
      }
      if (!this.state.portalMessage && !this.state.isANewPortalMessage) {
         return
      }
      var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

      changeActiveTabStyle(this.state.tabs, page, this.props.colors)

      var context = ''
      if (page === 'data') {
         context =
            <Box sx={{ flexGrow: 1 }}>
               <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                  <Grid item md={2}><MainTextField {...this.props} type='number' id='idportalmensagem' value={this.state.portalMessage.idportalmensagem} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>

                  {/* Inputs de Datas */}
                  <Grid item md={3}><MainDateTimeInput {...this.props} id='datainicial' value={this.state.portalMessage.datainicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                  <Box
                     display='flex'
                     justifyContent='center'
                     alignItems='center'
                     paddingTop='15px'
                     marginRight='5px'
                  >
                     <span>até</span>
                  </Box>
                  <Grid item md={3}><MainDateTimeInput {...this.props} id='datafinal' value={this.state.portalMessage.datafinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>

                  <Grid sx={{ marginTop: '15px' }} item md={12}><MainTextField required {...this.props} id='mensagem' value={this.state.portalMessage.mensagem} label='Mensagem' handleChange={this.handleChangeTextTab} /></Grid>

                  <Box
                     sx={{
                        mr: '45px',
                        display: 'grid',
                        gap: '15px',
                        gridTemplateColumns: {
                           sm: '50% 50%',
                           md: '20% 20% 20% 20% 20%',
                        },
                        width: '85%',
                        marginLeft: '15px',
                        marginTop: '20px',
                     }}

                  >
                     <MainCheckBoxInput {...this.props} id='vendedor' value={this.state.portalMessage.vendedor} label='Vendedor' handleChange={this.handleChangeTextTab} />
                     <MainCheckBoxInput {...this.props} id='varejo' value={this.state.portalMessage.varejo} label='Varejo PDV' handleChange={this.handleChangeTextTab} />
                     <MainCheckBoxInput {...this.props} id='clienteb2b' value={this.state.portalMessage.clienteb2b} label='Cliente B2B' handleChange={this.handleChangeTextTab} />
                     <MainCheckBoxInput {...this.props} id='clienteb2c' value={this.state.portalMessage.clienteb2c} label='Cliente B2C' handleChange={this.handleChangeTextTab} />
                     <MainCheckBoxInput {...this.props} id='representante' value={this.state.portalMessage.representante} label='Representante' handleChange={this.handleChangeTextTab} />
                  </Box>

                  <MainTabButton sx={{ width: { sm: '93%', md: '15%'}, margin: '20px 0 0 7px' }} {...this.props} onButtonClick={this.saveOrUpdatePortalMessage} title="Salvar" />

               </Grid>
            </Box>
      }
      ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
   }

   handleChangeText = (event) => {
      this.setState({
         [event.target.id]: event.target.value,
      })
   }

   handleChangeTextTab = (event) => {
      handleChangeText(this.state.portalMessage, event.target.id, event.target.value, () => this.handleChangeTab())
   }

   onCloseEditTab = () => {
      this.setState({
         isLoadingTab: true,
         portalMessage: {},
      })
   }

   onPortalMessageTableChange = (page) => {
      let config = {
         method: 'get',
         endpoint: 'message/portal/search'
      }
      let form = {
         page: page,
         term: this.state.search,
         messageCode: this.state.messageCode,
         isCurrent: this.state.isCurrent,
         isExpired: this.state.isExpired
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            this.setState({
               portalMessageList: r.data.portal_message,
               portalMessageColumns: r.data.columns,
               portalMessageTotalSize: r.data.total_size,

               isLoading: false,
               isLoadingPortalMessageTable: false,
            })
         }
      })
   }

   saveOrUpdatePortalMessage = () => {
      let config = {
         method: 'post',
         endpoint: 'message/portal/single'
      }
      let form = {
         id: this.state.portalMessage.idportalmensagem,
         portalMessage: this.state.portalMessage,
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            var newState = {
               alertMessage: r.data.message,
               alertType: 'success',
               showAlert: true,
            }

            if (this.state.isANewPortalMessage) {
               newState['isANewPortalMessage'] = false
               this.closeEditTab()
            }

            this.setState(prevState => ({
               ...prevState, ...newState
            }))
         } else {
            this.setState({
               alertMessage: r.data.message,
               alertType: 'error',
               showAlert: true
            })
         }
      })
   }

   searchPortalMessageInfo = () => {
      let config = {
         method: 'get',
         endpoint: 'message/portal/single'
      }
      let form = {
         id: this.state.selectedRow.idportalmensagem
      }
      defaultRequest(config, form).then((r) => {
         if (r.status) {
            var portalMessageSingle = r.data.portal_message
            portalMessageSingle.vendedor = portalMessageSingle.vendedor === 'S'
            portalMessageSingle.varejo = portalMessageSingle.varejo === 'S'
            portalMessageSingle.clienteb2b = portalMessageSingle.clienteb2b === 'S'
            portalMessageSingle.clienteb2c = portalMessageSingle.clienteb2c === 'S'
            portalMessageSingle.representante = portalMessageSingle.representante === 'S'

            this.setState({
               portalMessage: portalMessageSingle,

               isLoadingTab: false,
            }, () => this.handleChangeTab())
         }
      })
   }


   render() {
      if (this.state.isLoading) {
         return (
            <></>
         )
      }
      return (
         <>
            {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
            <Box className='outline-box'>
               <Header {...this.props} title='Mensagens' menuId={this.state.menuId} showFav />
               <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                  <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                  <Box
                     sx={{
                        mr: '45px',
                        display: 'grid',
                        gap: '15px',
                        gridTemplateColumns: {
                           md: '100%',
                           lg: '10% 40% 17% 10% 10% 10%',
                        },
                     }}
                  >
                     <MainTextField {...this.props} type='number' id='messageCode' value={this.state.messageCode} label='Código' handleChange={this.handleChangeText} width='100%' />
                     <MainTextField {...this.props} id='search' value={this.state.search} label='Mensagem' handleChange={this.handleChangeText} width='100%' />
                     <Box
                        sx={{
                           mr: '45px',
                           display: 'grid',
                           gridTemplateColumns: {
                              sm: '50% 50%',
                              md: '100%',
                              xl: '50% 50%',
                           },
                           width: '100%',
                           border: '1px solid',
                           borderRadius: '5px',
                           paddingLeft: '8px',
                           borderColor: this.props.colors.grey[1100]
                        }}
                     >
                        <MainCheckBoxInput {...this.props} id='isCurrent' value={this.state.isCurrent} label='Vigente' handleChange={this.handleChangeText} />
                        <MainCheckBoxInput {...this.props} id='isExpired' value={this.state.isExpired} label='Vencido' handleChange={this.handleChangeText} />
                     </Box>
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onPortalMessageTableChange(0)}>Buscar</Button>
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ messageCode: '', search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                     <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewPortalMessage: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                  </Box>

                  <EditableTable
                     {...this.props}
                     id='idportal'
                     allowEdit
                     noDeleteButton
                     data={this.state.portalMessageList}
                     columns={this.state.portalMessageColumns}
                     rowId='idportalmensagem'
                     totalSize={this.state.portalMessageTotalSize}
                     onPageChange={this.onPortalMessageTableChange}
                     onEditRow={() => { }}
                     onRowDoubleClick={(params) => this.createEditTab(params, false)}
                     isLoading={this.state.isLoadingPortalMessageTable}
                     extraColumnsConfig={
                        {
                            'idportalmensagem': {
                                'type': 'number',
                            },
                        }
                    }
                  />
               </Box>
            </Box>
         </>

      )
   }
}

export default PortalMessage;