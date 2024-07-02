import React from "react";

import DialogAlert from "./alerts/DialogAlert";

// Icons
import HelpIcon from '@mui/icons-material/Help';
import StarIcon from '@mui/icons-material/Star';
import StarBorderIcon from '@mui/icons-material/StarBorder';

import { Box, IconButton, Typography } from "@mui/material";
import { defaultRequest } from "../utils/request/request";


class Header extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            isFavorited: false,
            showBox: false
        }
    }

    componentDidMount() {
        if(this.props.showFav) {
            let config = {
                method: 'get',
                endpoint: 'menu/favorite'
            }
            
            let form = {
                menuId: this.props.menuId,
                userId: this.props.user.IDUsuario
            }
    
            defaultRequest(config, form).then((r) => {
                if(r.status){
                    this.setState({
                        isFavorited: r.data.is_favorited
                    })
                }
            })
        }
    }

    handleClose = () => {
        this.setState({showBox: false})
    }

    handleFavorite = () => {
        let config = {
            method: this.state.isFavorited ? 'delete' : 'post',
            endpoint: 'menu/favorite'
        }
        
        let form = {
            menuId: this.props.menuId,
            userId: this.props.user.IDUsuario
        }

        defaultRequest(config, form).then((r) => {
            if(r.status){
                this.setState({
                    isFavorited: !this.state.isFavorited
                })
            }
        })
    }

    handleHelpBox = () => {
        this.setState({showBox: true})
    }

    render() {
        return(
            <Box mb='10px'>
                <Box display='flex'> 
                    <Typography fontSize='1.5rem' variant={this.props.variant ?? 'h2'} color={this.props.color ?? this.props.colors.custom['text']} fontWeight='bold'>  {/*this.props.colors.grey[100] */}
                        {this.props.title}
                    </Typography>
                    {this.props.showFav ?
                        <Box height='30px' display='flex' alignItems='center'>
                            {/* <IconButton>
                                {this.state.isFavorited ?
                                    <StarIcon onClick={this.handleFavorite}/>
                                :
                                    <StarBorderIcon onClick={this.handleFavorite}/>
                                }
                            </IconButton>
                            <IconButton onClick={this.handleHelpBox}>
                                <HelpIcon />
                            </IconButton> */}
                            <DialogAlert {...this.props} isOpen={this.state.showBox} onClose={this.handleClose} title={'Tutorial'} body={<Typography>Ola</Typography>} />
                        </Box> : <></> }
                </Box>
                
                <Typography variant='h5' color={this.props.colors.blueAccent[400]}>{this.props.subtitle}</Typography>
                
            </Box>
        )
    }
}

export default Header