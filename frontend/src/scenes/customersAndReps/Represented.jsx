import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import LoadingGif from "../../components/visual/LoadingGif";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

// Icons
import SearchIcon from '@mui/icons-material/Search';

import { addLastAccess, changeActiveTabStyle, createEditTab } from "../../utils/layout";
import { Box, Button, Grid, IconButton, Typography } from "@mui/material";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";
import { searchCEP } from "../../utils/request/apiRequest";


class Represented extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            menuId: '5',
            isLoading: true,
            isLoadingTab: true,
            isLoadingRepresentedTable: true,
            isLoadingRepresentativeTable: true,
            isLoadingLocalSaleTable: true,
            isLoadingSalesRegionTable: true,

            localSaleOption: '',
            mainLocalSale: '',
            salesRegionOption: '',
            search: '',
            status: '',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Cancelado' }
            ],
            comissionPolicyFullOptions: [],
            productLineOptions: [],
            localSaleOptions: [],
            mainLocalSaleOptions: [],
            salesRegionOptions: [],
            salesTeamOptions: [],

            comissionPolicy: {},
            represented: {},

            localSaleList: [],
            localSaleColumns: [],
            localSaleTotalSize: '',

            representedList: [],
            representedColumns: [],
            representedTotalSize: '',

            representativeList: [],
            representativeColumns: [],
            representativeTotalSize: '',

            salesRegionList: [],
            salesRegionColumns: [],
            salesRegionTotalSize: '',

            activeTab: 'infos',
            tabs: [
                { id: 'infos', title: 'Dados' },
                { id: 'config', title: 'Configurações' },
                { id: 'representative', title: 'Representantes' },
                { id: 'salesRegion', title: 'Região de Vendas' },
                { id: 'localSale', title: 'Locais de Vendas' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        optionsRequest(this, ['city', 'comissionPolicyFull', 'localSale', 'productLine', 'salesRegion', 'salesTeam'])
        this.onRepresentedTableChange(0)
    }

    addLocalSale = () => {
        if (!this.state.localSaleOption) {
            this.setState({
                alertType: 'error',
                alertMessage: 'Selecione um local para adicionar',
                showAlert: true,
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'represented/localsale'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada,
            localSaleId: this.state.localSaleOption
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    isLoadingLocalSaleTable: true
                }, () => { this.handleChangeTab() })
            } else {
                this.setState({
                    alertType: 'error',
                    alertMessage: r.data.message,
                    showAlert: true,
                })
            }
        })
    }

    changeEditTab = () => {
        createEditTab('Informações da Representada', this.state.tabs, this.props, (event) => this.handleChangeTab(event))
    }

    createEditTab = (params) => {
        this.setState({ selectedRow: params, isLoadingTab: true }, () => createEditTab('Dados Representada', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deleteLocalSale = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'represented/localsale'
        }
        let form = {
            id: this.state.selectedRow.idrepresentada,
            localSaleId: id
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    isLoadingLocalSaleTable: true
                }, () => { this.handleChangeTab() })
            } else {
                this.setState({
                    alertType: 'error',
                    alertMessage: r.data.message,
                    showAlert: true,
                })
            }
        })
    }

    handleChangeRepresentedStatus = (event) => {
        var represented = this.state.represented
        represented.situacao = represented.situacao === 'A' ? 'X' : 'A'

        let config = {
            method: 'post',
            endpoint: 'represented/status'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada,
            status: represented.situacao
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    represented: represented
                }, () => this.handleChangeTab())
            }
        })
    }

    handleChangeComissionPolicy = (event) => {
        let represented = this.state.represented
        represented.idpolcomissao = event.target.value
        this.setState({
            comissionPolicy: this.state.comissionPolicyFullOptions.find(obj => obj.idpolcomissao === event.target.value),
            represented: represented
        }, () => this.handleChangeTab())
    }

    handleChangeMainLocalSale = (event) => {
        let config = {
            method: 'post',
            endpoint: 'represented/localsale/main'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada,
            localSaleId: event.target.value
        }

        defaultRequest(config, form).then((r) => {
            this.setState({
                mainLocalSale: event.target.value,
                alertType: r.status ? 'success' : 'error',
                alertMessage: r.data.message,
                showAlert: true,
            }, () => this.handleChangeTab())
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchRepresentedInfo())
            return
        }
        if (!this.state.represented) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'infos') {
            context =
                <>
                    <Box sx={{ flexGrow: 1 }}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='coderp' value={this.state.represented.coderp || ''} label='Código ERP' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='cnpj' value={this.state.represented.cnpj || ''} label='CNPJ/CPF' handleChange={this.handleChangeTextRepresented} /></Grid>
                            <Grid item md={3}><MainSelectInput {...this.props} disabled id='situacao' value={this.state.represented.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextRepresented} /></Grid>
                            <Grid item md={3}>
                                <MainTabButton width='94%' {...this.props} onButtonClick={this.handleChangeRepresentedStatus} title={this.state.represented.situacao === 'A' ? 'Inativar' : 'Ativar'} />
                            </Grid>
                            <Grid item md={6}><MainTextField {...this.props} disabled id='razao' value={this.state.represented.razao || ''} label='Razão Social' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={6}><MainTextField {...this.props} disabled id='fantasia' value={this.state.represented.fantasia || ''} label='Fantasia' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            {/* Address info */}
                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Endereço" /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='cep' value={this.state.represented.cep || ''} label='CEP' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={5}><MainTextField {...this.props} disabled id='logradouro' value={this.state.represented.logradouro || ''} label='Logradouro' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} disabled id='bairro' value={this.state.represented.bairro || ''} label='Bairro' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='numero' value={this.state.represented.numero || ''} label='Número' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='complemento' value={this.state.represented.complemento || ''} label='Complemento' handleChange={this.handleChangeTextRepresented} width={{ xs: '97%', sm: '97%', md: '95%' }} /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} disabled id='cidade' value={this.state.represented.cidade} label='Cidade' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={2}><MainTextField {...this.props} disabled id='uf' value={this.state.represented.uf || ''} label='UF' handleChange={this.handleChangeTextRepresented} width={{ xs: '97%', sm: '97%', md: '92%' }} /></Grid>
                            {/* Personal info */}
                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Contatos" /></Grid>
                            <Grid item md={6}><MainTextField {...this.props} disabled id='email' value={this.state.represented.email || ''} label='Email' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='telfixo' value={this.state.represented.telfixo || ''} label='Telefone Fixo' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='telcelular' value={this.state.represented.telcelular || ''} label='Telefone Celular' handleChange={this.handleChangeTextRepresented} width={{ xs: '97%', sm: '97%', md: '92%' }} /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='whatsapp' value={this.state.represented.whatsapp || ''} label='Whatsapp' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='datafundacao' value={this.state.represented.datafundacao || ''} label='Data Fundação' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='inscmunicipal' value={this.state.represented.inscmunicipal || ''} label='Inscrição Municipal' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='inscestadual' value={this.state.represented.inscestadual || ''} label='Inscrição Estadual' handleChange={this.handleChangeTextRepresented} width={{ xs: '97%', sm: '97%', md: '92%' }} /></Grid>
                        </Grid>
                    </Box>
                </>
        } else if (page === 'config') {
            context =
                <>
                    <Box sx={{ flexGrow: 1 }}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={6}><MainSelectInput {...this.props} disabled id='idequipe' value={this.state.represented.idequipe || ''} optionsList={this.state.salesTeamOptions} label='Equipe de Venda' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={6}><MainSelectInput {...this.props} disabled id='idlinha' value={this.state.represented.idlinha || ''} optionsList={this.state.productLineOptions} label='Linha de Produtos' handleChange={this.handleChangeTextRepresented} fullWidth /></Grid>
                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Política de Comissão" /></Grid>
                            <Grid item md={9}><MainSelectInput {...this.props} id='idpolcomissao' value={this.state.represented.idpolcomissao || ''} optionsList={this.state.comissionPolicyFullOptions} label='' handleChange={this.handleChangeTextRepresented} width='97.5%' /></Grid>

                            <Grid item md={3}>
                                <MainTabButton width={{ xs: '97%', sm: '97%', md: '94%' }} {...this.props} onButtonClick={this.saveComissionPolicy} title="Salvar" />
                            </Grid>

                            <Grid item md={2}><MainTextField {...this.props} id='idpolcomissao' disabled value={this.state.comissionPolicy.idpolcomissao || ''} label='Código' handleChange={this.handleChangeTextComissionPolicy} fullWidth /></Grid>
                            <Grid item md={7}><MainTextField {...this.props} id='descomissao' value={this.state.comissionPolicy.despolitica || ''} label='Descrição da Política' handleChange={this.handleChangeTextComissionPolicy} fullWidth /></Grid>
                            <Grid item md={3}><MainSelectInput {...this.props} id='situacao' value={this.state.comissionPolicy.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeComissionPolicy} width={{ xs: '97%', sm: '97%', md: '94%' }} /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} id='percomissao' value={this.state.comissionPolicy.percomissao || ''} label='Comissão Carteira (%)' handleChange={this.handleChangeComissionPolicy} fullWidth /></Grid>
                            <Grid item md={3}><MainTextField {...this.props} id='percomnovos' value={this.state.comissionPolicy.percomnovos || ''} label='Comissão Novos (%)' handleChange={this.handleChangeComissionPolicy} fullWidth /></Grid>
                        </Grid>
                    </Box>
                </>
        } else if (page === 'representative') {
            if (this.state.isLoadingRepresentativeTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onRepresentativeTableChange(0))
                return
            }
            context =
                <>
                    <EditableTable
                        {...this.props}
                        id='representativeTable'
                        data={this.state.representativeList}
                        columns={this.state.representativeColumns}
                        totalSize={this.state.representativeTotalSize}
                        rowId={'idusuario'}
                        onRowDoubleClick={() => { }}
                        onPageChange={this.onRepresentatitiveTableChange}
                        isLoading={this.state.isLoadingRepresentativeTable}
                    />
                </>
        } else if (page === 'salesRegion') {
            if (this.state.isLoadingSalesRegionTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onSalesRegionTableChange(0))
                return
            }
            context =
                <>
                    <EditableTable
                        {...this.props}
                        id='representativeTable'
                        data={this.state.salesRegionList}
                        columns={this.state.salesRegionColumns}
                        totalSize={this.state.salesRegionTotalSize}
                        rowId={'idlocalvenda'}
                        onPageChange={this.onSalesRegionTableChange}
                        isLoading={this.state.isLoadingSalesRegionTable}
                    />
                </>
        } else if (page = 'localSale') {
            if (this.state.isLoadingLocalSaleTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onLocalSaleTableChange(0))
                return
            }
            context =
                <>
                    <Box sx={{ flexGrow: 1 }}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={9}><MainSelectInput required {...this.props} id='localSaleOption' value={this.state.localSaleOption} optionsList={this.state.localSaleOptions} label='Local de Venda' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                            <Grid item md={3}>
                                <MainTabButton width='96.5%' {...this.props} onButtonClick={this.addLocalSale} title="Inserir" />
                            </Grid>
                        </Grid>
                    </Box>
                    <EditableTable
                        {...this.props}
                        height='45vh'
                        allowEdit
                        noEditButton
                        id='representativeTable'
                        data={this.state.localSaleList}
                        columns={this.state.localSaleColumns}
                        totalSize={this.state.localSaleTotalSize}
                        rowId={'idlocalvenda'}
                        onEditRow={this.onLocalSaleTableEdit}
                        onPageChange={this.onLocalSaleTableChange}
                        isLoading={this.state.isLoadingLocalSaleTable}
                    />
                    <Box sx={{ flexGrow: 1 }}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={6}><MainSelectInput {...this.props} id='mainLocalSale' value={this.state.mainLocalSale || ''} optionsList={this.state.mainLocalSaleOptions} label='Local Padrão' handleChange={this.handleChangeMainLocalSale} fullWidth /></Grid>
                        </Grid>
                    </Box>
                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextComissionPolicy = (event) => {
        handleChangeText(this.state.comissionPolicy, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextRepresented = (event) => {
        handleChangeText(this.state.represented, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            represented: {},
            comissionPolicy: {},
            localSaleOption: '',
            isLoadingTab: true,
            isLoadingLocalSaleTable: true,
            isLoadingRepresentativeTable: true,
            isLoadingSalesRegionTable: true,
            activeTab: 'infos'
        })
    }

    onLocalSaleTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                customerContactList: row
            }, () => this.deleteLocalSale(extraParam))
        }
    }

    onLocalSaleTableChange = (page) => {
        this.setState({
            isLoadingLocalSaleTable: true
        })
        let config = {
            method: 'get',
            endpoint: 'represented/localsale'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    mainLocalSale: r.data.main_local_sale?.idlocalvenda,
                    mainLocalSaleOptions: r.data.main_local_sale_option,
                    localSaleList: r.data.local_sale,
                    localSaleColumns: r.data.columns,
                    localSaleTotalSize: r.data.total_size,
                    isLoadingLocalSaleTable: false,
                    activeTab: 'localSale'
                }, () => this.handleChangeTab())
            }
        })
    }

    onRepresentativeTableChange = (page) => {
        this.setState({
            isLoadingRepresentativeTable: true
        })
        let config = {
            method: 'get',
            endpoint: 'representative/search'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada,
            page: page,
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    representativeList: r.data.representative,
                    representativeColumns: r.data.columns,
                    representativeTotalSize: r.data.total_size > 999 ? 999 : r.data.total_size,
                    isLoadingRepresentativeTable: false,
                    activeTab: 'representative'
                }, () => this.handleChangeTab())
            }
        })
    }

    onRepresentedTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'represented/search'
        }

        let form = {
            page: page,
            term: this.state.search,
            status: this.state.status
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    representedList: r.data.represented,
                    representedColumns: r.data.columns,
                    representedTotalSize: r.data.total_size > 999 ? 999 : r.data.total_size,
                    isLoading: false,
                    isLoadingRepresentedTable: false
                })
            }
        })
    }

    saveComissionPolicy = () => {
        let config = {
            method: 'post',
            endpoint: 'represented/comissionpolicy'
        }
        let form = {
            id: this.state.selectedRow.idrepresentada,
            comissionPolicy: this.state.comissionPolicy
        }

        defaultRequest(config, form).then((r) => {
            this.setState({
                alertType: r.status ? 'success' : 'error',
                alertMessage: r.data.message,
                showAlert: true,
            })
        })
    }

    searchRepresentedInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'represented/single'
        }

        let form = {
            id: this.state.selectedRow.idrepresentada
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var represented = r.data.represented
                searchCEP(represented.cep).then((r) => {
                    const cityUF = r

                    represented.cidade = cityUF.city
                    represented.uf = cityUF.uf
                    this.setState({
                        represented: represented,
                        comissionPolicy: this.state.comissionPolicyFullOptions.find(obj => obj.idpolcomissao === represented.idpolcomissao),
                        isLoadingTab: false
                    }, () => this.handleChangeTab())
                })
            }
        })
    }


    render() {
        if (this.state.isLoading) {
            return <></>
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Representadas' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '30px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '60% 20% 20%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Pesquisar' inputProps={<IconButton onClick={() => this.setState({ isLoadingRepresentedTable: true }, this.onRepresentedTableChange(0))}><SearchIcon /></IconButton>} handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} needNoneOption width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onRepresentedTableChange(0)}>Buscar</Button>
                        </Box>
                        <EditableTable
                            {...this.props}
                            id='representedTable'
                            allowEdit
                            data={this.state.representedList}
                            columns={this.state.representedColumns}
                            rowId={'idrepresentada'}
                            totalSize={this.state.representedTotalSize}
                            onPageChange={this.onRepresentedTableChange}
                            onRowDoubleClick={this.createEditTab}
                            isLoading={this.state.isLoadingRepresentedTable}
                            extraColumnsConfig={
                                {
                                    'idrepresentada': {
                                        'type': 'number'
                                    },
                                    'coderp': {
                                        'type': 'number'
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

export default Represented