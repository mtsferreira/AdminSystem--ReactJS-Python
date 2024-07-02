import React from "react";

import { Box, Button, Grid, InputAdornment, TextField, Typography } from "@mui/material";
import { defaultRequest } from "../../utils/request/request";

// Icons
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';

// Images
import logo from "../../data/logo1.png";
import bg from "../../data/bg.png";

class Login extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            showAlert: false,
            alertMessage: '',
            alertType: null,
            email: '',
            password: '',
            showPassword: false
        }
    }

    handleChange = (event) => {
        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    logIn = () => {
        // REQUEST PARA VALIDAÇÃO DE DADOS

        let config = {
            method: 'get',
            endpoint: 'login'
        }

        let form = {
            email: this.state.email,
            password: this.state.password
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                localStorage.setItem('userToken', r.data.token)
                window.location.href = '/#/'
                window.location.reload()
            } else {
                this.setState({ showAlert: true, alertType: 'error', alertMessage: r.data.message })
            }
        })
    }

    render() {
        return (
            <Box
                display='grid'
                height='100vh'
                width='100vw'
                sx={{ backgroundImage: `url(${bg})`, backgroundSize: 'cover' }}
            >
                {/* {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({showAlert:false, alertMessage:''})}/> : <></>} */}
                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: 'auto' }}>
                    <Box component='img' src={logo} sx={{ height: '80%', width: '80%' }} />
                    <Box id='login-box' sx={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-around', height: '380px', width: '85%', backgroundColor: "white", borderRadius: '20px', padding: '5px 20px' }}>

                        <Box m='10px 0 30px 0'>
                            <Grid container>
                                <Grid item md={12} sx={{ textAlign: 'center' }}><Typography variant="h6">AUTOMAÇÃO DA <br />FORÇA DE VENDAS</Typography></Grid>
                            </Grid>
                        </Box>

                        <Box mb='20px'>
                            <TextField
                                id='email'
                                value={this.state.email}
                                onChange={(event) => this.handleChange(event)}
                                placeholder='Email'
                                size='small'
                                fullWidth
                                sx={{
                                    '& .MuiInputBase-root': {
                                        borderRadius: '12px',
                                    },
                                    borderRadius: '12px',
                                    backgroundColor: '#F7F7F7',
                                    '& fieldset': {
                                        borderRadius: '12px',
                                        border: '2px solid #E5E5E5',
                                    },
                                    '&:hover fieldset': {
                                        borderColor: 'none !important'
                                    }
                                }}
                            />
                        </Box>
                        <Box mb='20px'>
                            <TextField
                                id='password'
                                type={this.state.showPassword ? 'text' : 'password'}
                                value={this.state.password}
                                onChange={(event) => this.handleChange(event)}
                                placeholder='Senha'
                                size='small'
                                fullWidth
                                sx={{
                                    borderRadius: '12px',
                                    backgroundColor: '#F7F7F7',
                                    '& .MuiInputBase-root': {
                                        borderRadius: '12px',
                                    },
                                    '& fieldset': {
                                        borderRadius: '12px',
                                        border: '2px solid #E5E5E5'
                                    },
                                    '&:hover fieldset': {
                                        borderColor: 'none !important'
                                    }
                                }}
                                InputProps={{
                                    endAdornment: (
                                        <InputAdornment position="start" onClick={() => this.setState({ showPassword: !this.state.showPassword })} sx={{ 'cursor': 'pointer' }}>
                                            {this.state.showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
                                        </InputAdornment>
                                    ),
                                }}
                            />
                        </Box>
                        {this.state.showAlert ?
                            <Box mb='20px' textAlign='center'>
                                <Typography color='#cf1508'>{this.state.alertMessage}</Typography>
                            </Box>
                            : <></>}
                        <Box sx={{ display: 'flex', alignItems: 'center' }}>
                            <Button
                                onClick={this.logIn}
                                fullWidth
                                variant='contained'
                                style={{ border: 'none', borderRadius: '30px', height: '40px', width: '35%', margin: '0 auto' }}
                                sx={{
                                    '& .MuiButton-root': {
                                        height: '40px',
                                        borderRadius: '12px',
                                    }
                                }}
                            >
                                <Typography>Entrar</Typography>
                            </Button>
                        </Box>

                        <Box>
                            <Box m='20px 0 5px 0' width='auto' textAlign='center'>
                                <Typography variant="h7">Desenvolvido por Mateus Rumão</Typography>
                            </Box>
                            <Box width='auto' textAlign='center'>
                                <Typography variant="h7" color='grey'>v 1.0.18</Typography>
                            </Box>
                        </Box>
                    </Box>
                </Box>
            </Box>
        )
    }
}

export default Login