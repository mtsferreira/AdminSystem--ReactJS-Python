import React from "react";

import Header from "../../components/Header";
import MainImageUpload from "../../components/inputs/MainImageUpload";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess } from "../../utils/layout";
import { Box, Grid } from "@mui/material";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { searchCEP } from "../../utils/request/apiRequest";
import { handleChangeCep, handleChangeImage, handleChangeText } from "../../utils/handleChange";

class Company extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            isLoading: true,
            menuId: '14',
            cnpj: '',

            company: {},
            cityOptions: []
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        optionsRequest(this, ['city'])
        this.searchCompany()
    }

    handleChangeCep = (event) => {
        handleChangeCep(this, this.state.company, 'company', event, () => { })
    }

    handleChangeImage = (hexString, fieldName) => {
        handleChangeImage(this, this.state.company, hexString, fieldName, () => { })
    }

    handleChangeText = (event) => {
        handleChangeText(this.state.company, event.target.id, event.target.value, () => { this.setState(prevState => ({ ...prevState })) })
    }

    saveCompanyChanges = () => {
        let config = {
            method: 'post',
            endpoint: 'company'
        }

        let form = {
            companyId: this.state.company.idempresa,
            company: this.state.company
        }

        defaultRequest(config, form).then((r) => {
            this.setState({
                alertMessage: r.data.message,
                alertType: r.status ? 'success' : 'error',
                showAlert: true
            })
        })
    }

    searchCompany = () => {
        let config = {
            method: 'get',
            endpoint: 'company'
        }

        let form = {
            cnpj: this.state.cnpj
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                searchCEP(r.data.company.cep).then((res) => {
                    var company = r.data.company
                    company.cidade = res.city
                    this.setState({
                        company: company,
                        isLoading: false
                    })
                }).catch((error) => {
                    this.setState({
                        company: r.data.company,

                        alertMessage: 'CEP não encontrado',
                        alertType: 'error',
                        showAlert: true
                    })
                })
            }
        })
    }

    render() {
        if (this.state.isLoading) {
            return (<></>)
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Empresa Controladora' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', md: 'column', lg: 'row' }, margin: '15px 0' }}>
                            <Grid item md={2}><MainTextField {...this.props} type='number' disabled id='idempresa' value={this.state.company.idempresa || ''} label='Código' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField required {...this.props} id='cnpj' value={this.state.company.cnpj || ''} label='CNPJ' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={7}><MainTextField required {...this.props} id='fantasia' value={this.state.company.fantasia || ''} label='Fantasia' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={12}><MainTextField required {...this.props} id='razao' value={this.state.company.razao || ''} label='Razão' handleChange={this.handleChangeText} width={{ xs: '97%', sm: '97%', md: '98.3%' }} /></Grid>

                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubSubTitle" label="Endereço" /></Grid>
                            <Grid item md={2}><MainTextField required {...this.props} type='number' id='cep' value={this.state.company.cep || ''} label='CEP' handleChange={this.handleChangeCep} fullWidth /></Grid>
                            <Grid item md={5}><MainTextField required {...this.props} id='logradouro' value={this.state.company.logradouro || ''} label='Logradouro' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={2}><MainTextField required {...this.props} type='number' id='numero' value={this.state.company.numero || ''} label='Número' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} id='complemento' value={this.state.company.complemento || ''} label='Complemento' handleChange={this.handleChangeText} width={{ xs: '97%', sm: '97%', md: '93%' }} /></Grid>
                            <Grid item md={3}><MainTextField required {...this.props} id='bairro' value={this.state.company.bairro || ''} label='Bairro' handleChange={this.handleChangeText} fullWidth /></Grid>
                            <Grid item md={3}><MainSelectInput required {...this.props} searchByLabel id='codibge' value={this.state.company.cidade || ''} optionsList={this.state.cityOptions} label='Cidade' handleChange={this.handleChangeText} fullWidth /></Grid>

                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubSubTitle" label="Imagens" /></Grid>
                            <Box
                                display='flex'
                                flexDirection='row'
                                justifyContent='center'
                                alignItems='center'
                                width='450px'
                                height='260px'
                                border='2px solid'
                                borderRadius='5px'
                                // paddingTop='25px'
                                position='relative'
                                borderColor={this.props.colors.grey[1100]}

                                marginLeft='7px'
                                marginTop='20px'
                            >
                                {/* <span style={{ position: 'absolute', fontSize: '15px', top: '0' }}>Imagens:</span> */}
                                <MainImageUpload sx={{ margin: '0 10px' }} {...this.props} id='imagem' src={this.state.company.imagem} label='Imagem:' handleChangeImage={this.handleChangeImage} />

                                <MainImageUpload sx={{ margin: '0 10px' }} {...this.props} id='banner' src={this.state.company.banner} label='Banner:' handleChangeImage={this.handleChangeImage} />

                            </Box>

                            <Box
                                display='flex'
                                justifyContent='center'
                                borderRadius='5px'
                                backgroundColor={this.props.colors.custom['mainButton']}
                                onClick={this.saveCompanyChanges}
                                width='170px'
                                height='40px'

                                marginTop='20px'
                                marginLeft='15px'
                            >
                                <MainTabButton width='100%' {...this.props} onButtonClick={this.saveCompanyChanges} title="Salvar" />
                            </Box>

                        </Grid>
                    </Box>
                </Box>
            </>
        )
    }
}

export default Company