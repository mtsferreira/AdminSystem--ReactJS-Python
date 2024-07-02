import React from "react";

// Icons
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';

// Images
import logo from "../../data/logo2.png";

import { Avatar, Box, IconButton, Menu, MenuItem, Typography } from '@mui/material';
import { defaultRequest } from "../../utils/request/request";
import { displayImage } from "../../utils/file";


class Navbar extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isCollapsed: false,
            hoverSidebar: false,
            anchorElement: null,
            open: false,
            userImage: null,
        }
    }

    componentDidMount() {
        let config = {
            method: 'get',
            endpoint: 'user/image'
        }
        let form = {
            id: this.props.user.IDUsuario
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    userImage: r.data.foto,
                })
            }
        })
    }

    handleCollapse = () => {
        this.setState({
            isCollapsed: !this.state.isCollapsed,
            hoverSidebar: !this.state.hoverSidebar
        }, () => {
            this.props.handleCollapse(this.state.isCollapsed)
        })
    }

    handleClose = () => {
        this.setState({
            anchorElement: null,
            open: false
        })
    }

    handleOpen = (e) => {
        this.setState({
            anchorElement: e.currentTarget,
            open: this.state.open ? false : true
        })
    }

    logOff = () => {
        localStorage.removeItem('userToken')
        window.location.reload()
    }

    render() {
        return (
            <Box display='flex' className='navbar' justifyContent='space-between' padding='10px' backgroundColor={this.props.colors.custom['bars']} sx={{ borderBottom: '0.5px solid #00000050' }}>

                <Box
                    display="flex"
                    justifyContent="space-between"
                    style={{
                        margin: 'auto 0',
                        color: this.props.colors.grey[100]
                    }}
                >
                    <Box
                        component='img'
                        src={logo}
                        onClick={() => { window.location.href = '#/' }}
                        sx={{
                            maxHeight: '50px',
                            cursor: 'pointer'
                        }}
                    />
                    <IconButton sx={{ marginLeft: '15px' }} onClick={this.handleCollapse}>
                        <MenuOutlinedIcon sx={{ color: this.props.colors.custom['barsIconsAndTexts'] }} />
                    </IconButton>
                </Box>

                {/* ICONS */}
                <Box
                    display='flex'
                    mr='10px'
                    sx={{
                        '& .MuiPaper-root': {
                            backgroundColor: `${this.props.colors.primary[400]} !important`
                        }
                    }}
                >
                    <IconButton>
                        <SettingsOutlinedIcon sx={{ color: this.props.colors.custom['barsIconsAndTexts'] }} />
                    </IconButton>
                    <Box textAlign='center' m='0 10px'>
                        <IconButton onClick={this.handleOpen} sx={{ padding: '0', paddingBottom: '5px' }}>
                            <Avatar src={this.state.userImage ? displayImage(this.state.userImage) : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/2048px-User-avatar.svg.png"} />
                            <Menu anchorEl={this.state.anchorElement} open={this.state.open} onClose={this.handleClose}>
                                <MenuItem onClick={this.logOff}>Sair</MenuItem>
                            </Menu>
                        </IconButton>
                        <Typography fontSize='10px' letterSpacing='0.5px' sx={{ 'cursor': 'pointer', color: this.props.colors.custom['barsIconsAndTexts'] }} onClick={this.handleOpen}>
                            {this.props.user.Nome + ' ' + this.props.user.Sobrenome}
                        </Typography>
                    </Box>
                </Box>
            </Box>
        )
    }
}

export default Navbar