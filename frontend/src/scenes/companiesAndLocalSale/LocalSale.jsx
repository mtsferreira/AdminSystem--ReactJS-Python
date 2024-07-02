import React from "react";
import ReactDOM from "react-dom";

import Accordion from "../../components/visual/Accordion";
import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import LoadingGif from "../../components/visual/LoadingGif";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainImageUpload from "../../components/inputs/MainImageUpload";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess, changeActiveTabStyle, createEditTab } from "../../utils/layout";
import { Box, Button, Grid, Typography } from "@mui/material";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeCep, handleChangeImage, handleChangeText } from "../../utils/handleChange";
import { searchCEP } from "../../utils/request/apiRequest";


class LocalSale extends React.Component {
    constructor(props) {
        super(props)
        this.newEmailRef = React.createRef()
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            isLoading: true,
            isLoadingTab: true,
            isLoadingEmailInfo: true,
            isLoadingLocalSaleTable: true,
            isLoadingLocalSaleEmailTable: true,

            menuId: '15',

            search: '',
            status: 'A',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'C', 'label': 'Cancelado' },
            ],

            isANewLocalSale: false,
            config: {},
            localSale: {},
            localEmail: {},
            localSaleList: [],
            localSaleColumns: {},
            localSaleTotalSize: '',

            newEmail: false,
            localSaleEmail: {},
            localSaleEmailList: [],
            localSaleEmailColumns: {},
            localSaleEmailTotalSize: '',

            activeTab: 'data',
            tabs: [
                { id: 'data', title: 'Dados' },
                { id: 'emailConfig', title: 'Configuração de E-mail' },
                { id: 'configurations', title: 'Configuração' },
            ],
        }
    }

    componentDidMount() {   // Carrega os informações antes da pagina ser renderizada. (pré-render)
        addLastAccess(this.state.menuId)
        this.onLocalSaleTableChange(0)
        optionsRequest(this, ['cascade', 'city', 'comissionDiscount', 'emailType', 'orderType', 'price', 'shippingCif', 'structurePrice', 'volume',])
    }

    componentDidUpdate() {
        if (this.state.newEmail) {
            if (this.newEmailRef.current) {
                this.newEmailRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onLocalSaleTableChange(0)
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({ selectedRow: params, isLoadingTab: true, tabs: [{ id: 'data', title: 'Dados' }], activeTab: 'data', localSale: { foto: '' } }, () => createEditTab('Criar Local de Venda', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewLocalSale: false,
                selectedRow: params,
                isLoadingTab: true,
                tabs: [
                    { id: 'data', title: 'Dados' },
                    { id: 'emailConfig', title: 'Configuração de E-mail' },
                    { id: 'configurations', title: 'Configuração' },
                ],
                activeTab: 'data',
                config: {
                    habilitarmargemvalor: false,
                    visualizarsaldoestoque: false,
                    mostrabanner: false,
                    repetiritem: false,
                    permitirvendabloqueado: false,
                    habilitareventosdesconto: false,
                    liberardescontovolume: false,
                    habilitardescontocliente: false,
                    habilitardescontoadicional: false,
                    comissaocompartilhada: false,
                }
            }, () => createEditTab('Dados Locais de Venda', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteLocalSaleEmail = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'localsale/email'
        }
        let form = {
            id: id
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    handleChangeCep = (event) => {
        handleChangeCep(this, this.state.localSale, 'localSale', event, () => this.handleChangeTab())
    }

    handleChangeTab = (event) => {  // Abas
        if (this.state.isLoadingTab && !this.state.isANewLocalSale) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchLocalSaleInfo())
            return
        }
        if (!this.state.localSale && !this.state.isANewLocalSale) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Box
                        display='grid'
                        gridTemplateColumns='60% 40%'
                        gap='15px'
                        mr='15px'
                    >
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={4}><MainTextField required {...this.props} type='number' id='coderp' value={this.state.localSale.coderp || ''} label='Código ERP' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                            <Grid item md={4}><MainTextField required {...this.props} id='cnpj' value={this.state.localSale.cnpj || ''} label='CNPJ' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                            <Grid item md={4}><MainSelectInput required {...this.props} id='situacao' value={this.state.localSale.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '90%' }} /></Grid>
                            <Grid item md={12}><MainTextField required {...this.props} id='razao' value={this.state.localSale.razao || ''} label='Razão Social' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                            <Grid item md={12}><MainTextField required {...this.props} id='fantasia' value={this.state.localSale.fantasia || ''} label='Fantasia' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        </Grid>

                        <MainImageUpload {...this.props} id='foto' src={this.state.localSale.foto} handleChangeImage={this.handleChangeImage} handleChangeTab={this.handleChangeTab} />

                    </Box>

                    {/* Campos de Endereço */}
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Endereço" /></Grid>
                        <Grid item md={2}><MainTextField required {...this.props} type='number' id='cep' value={this.state.localSale.cep || ''} label='CEP' handleChange={this.handleChangeCep} fullWidth /></Grid>
                        <Grid item md={6}><MainTextField required {...this.props} id='logradouro' value={this.state.localSale.logradouro || ''} label='Logradouro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={4}><MainTextField required {...this.props} id='bairro' value={this.state.localSale.bairro || ''} label='Bairro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={2}><MainTextField required {...this.props} type='number' id='numero' value={this.state.localSale.numero || ''} label='Número' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput required {...this.props} searchByLabel id='codibge' value={this.state.localSale.cidade || ''} optionsList={this.state.cityOptions} label='Cidade' handleChange={this.handleChangeTextTab}  width={{ xs: '97%', sm: '97%', md: '96%' }} /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} id='complemento' value={this.state.localSale.complemento || ''} label='Complemento' handleChange={this.handleChangeTextTab} fullWidth /></Grid>

                        <Grid item md={2}>
                            <MainTabButton width='97%' {...this.props} onButtonClick={this.saveLocalSale} title="Salvar" />
                        </Grid>
                    </Grid>
                </Box >

        } else if (page === 'emailConfig') {
            if (this.state.isLoadingLocalSaleEmailTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onLocalSaleEmailTableChange(0))
                return
            }
            context =
                <>
                    <MainTabButton
                        sx={{ width: { xs: '100%', sm: '100%', md: '20%' }, mt: '15px' }}
                        {...this.props}
                        onButtonClick={() => { this.setState({ newEmail: true, isLoadingEmailInfo: false, localSaleEmail: {} }, () => this.handleChangeTab()) }}
                        title="Adicionar Novo"
                    />

                    <EditableTable
                        {...this.props}
                        noEditButton
                        allowEdit
                        height='50vh'
                        id='localsaleemailTable'
                        rowId='idlocalemail'
                        data={this.state.localSaleEmailList}
                        columns={this.state.localSaleEmailColumns}
                        totalSize={this.state.localSaleEmailTotalSize}
                        onEditRow={this.onLocalSaleEmailTableEdit}
                        onPageChange={this.onLocalSaleEmailTableChange}
                        onRowDoubleClick={(params) => this.onLocalSaleEmailTableDoubleClick(params)}
                        isLoading={this.state.isLoadingLocalSaleEmailTable}
                        extraColumnsConfig={
                            {
                                'idtipoemail_id': {
                                    'type': 'select',
                                    'options': this.state.emailTypeOptions
                                }
                            }
                        }
                    />

                    {this.state.newEmail ?
                        <>
                            <Box sx={{ flexGrow: 1 }}>
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                    <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Configuração Email" /></Grid>
                                    <Grid item md={3}><MainSelectInput required {...this.props} id='idtipoemail_id' value={this.state.localSaleEmail.idtipoemail_id || ''} optionsList={this.state.emailTypeOptions} label='Tipo de Email' handleChange={this.handleChangeTextTabEmail} fullWidth /></Grid>
                                    <Grid item md={5}><MainTextField required {...this.props} id='emailresposta' value={this.state.localSaleEmail.emailresposta || ''} label='Email Resposta' handleChange={this.handleChangeTextTabEmail} fullWidth /></Grid>

                                    <Grid item md={2}>
                                        <MainTabButton width='99%' {...this.props} onButtonClick={this.saveLocalSaleEmail} title="Salvar" />
                                    </Grid>

                                    <Grid item md={2}>
                                        <MainTabButton width='99%' {...this.props} onButtonClick={() => this.setState({ newEmail: false, isLoadingEmailInfo: true, localSaleEmail: {} }, () => this.handleChangeTab())} title="Cancelar" />
                                    </Grid>

                                    <Grid item md={12}><MainTextField required {...this.props} id='assunto' value={this.state.localSaleEmail.assunto || ''} label='Assunto' handleChange={this.handleChangeTextTabEmail} width={'100%'} /></Grid>
                                    <Grid item md={12}><MainTextField required {...this.props} id='corpo' value={this.state.localSaleEmail.corpo || ''} label='Corpo do Email' handleChange={this.handleChangeTextTabEmail} minRows={5} width={'100%'} /></Grid>
                                    <Grid ref={this.newEmailRef} item md={12}><MainTextField required {...this.props} id='assinatura' value={this.state.localSaleEmail.assinatura || ''} label='Assinatura' handleChange={this.handleChangeTextTabEmail} minRows={3} width={'100%'} /></Grid>
                                </Grid>
                            </Box>
                        </> : <></>}
                </>
        } else if (page === 'configurations') {
            context =
                <Box sx={{ flexGrow: 1, mr: '15px' }}>
                    <Accordion
                        {...this.props}
                        title='Configuração Geral'
                        customCss={{ margin: '5px 10px 20px 7px' }}
                        content={
                            <>
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                    <Grid item md={8}><MainSelectInput required {...this.props} id='preco' value={this.state.config.preco || ''} optionsList={this.state.priceOptions} label='Tabela de Preço' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={2}><MainTextField required {...this.props} type='number' id='coddeperp' value={this.state.config.coddeperp || ''} label='Depósito ERP' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={2}><MainTextField required {...this.props} type='number' id='prazomedio' value={this.state.config.prazomedio || ''} label='Prazo Médio' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={4}><MainSelectInput {...this.props} id='precoestrutura' value={this.state.config.precoestrutura || ''} optionsList={this.state.structurePriceOptions} label='Preço Por Estrutura' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={5}><MainSelectInput required {...this.props} id='idfretecif' value={this.state.config.idfretecif || ''} optionsList={this.state.shippingCifOptions} label='Frete Cif' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={3}><MainTextField required {...this.props} type='number' id='diasvalidade' value={this.state.config.diasvalidade || ''} label='Dias para Vencimento' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>
                                    <Grid item md={4}><MainSelectInput {...this.props} id='tipopedido' value={this.state.config.tipopedido || ''} optionsList={this.state.orderTypeOptions} label='Tipo de Pedido' handleChange={this.handleChangeTextTabConfig} fullWidth /></Grid>

                                    <Grid item md={8}><MainCheckBoxInput {...this.props} id='permitirvendabloqueado' value={this.state.config.permitirvendabloqueado} label='Permitir Venda a clientes Bloqueados' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='mostrabanner' value={this.state.config.mostrabanner} label='Exibir Banner no Orçamento' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={8}><MainCheckBoxInput {...this.props} id='visualizarsaldoestoque' value={this.state.config.visualizarsaldoestoque} label='Permitir visualização de Saldo' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='repetiritem' value={this.state.config.repetiritem} label='Permitir Itens Duplicados' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='habilitarmargemvalor' value={this.state.config.habilitarmargemvalor} label='Exibir Valor na Margem' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                </Grid>
                            </>
                        }
                    />
                    <Accordion
                        {...this.props}
                        title='Configuração de Descontos'
                        customCss={{ margin: '0 10px 20px 7px' }}
                        content={
                            <>
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                    <Grid item md={4}><MainSelectInput required {...this.props} id='desccomposto' value={this.state.config.desccomposto || ''} optionsList={this.state.cascadeOptions} label='Desconto Cascata' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainSelectInput required {...this.props} id='descvolume' value={this.state.config.descvolume || ''} optionsList={this.state.volumeOptions} label='Desconto Volume' handleChange={this.handleChangeTextTabConfig} /></Grid>

                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='habilitareventosdesconto' value={this.state.config.habilitareventosdesconto} label='Habilitar Eventos de Desconto' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='liberardescontovolume' value={this.state.config.liberardescontovolume} label='Habilitar Desconto de Volume' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='habilitardescontocliente' value={this.state.config.habilitardescontocliente} label='Habilitar Desconto do Cliente' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainCheckBoxInput {...this.props} id='habilitardescontoadicional' value={this.state.config.habilitardescontoadicional} label='Habilitar Desconto Adicional' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                </Grid>
                            </>
                        }
                    />
                    <Accordion
                        {...this.props}
                        title='Configuração de Comissão'
                        customCss={{ margin: '0 10px 20px 7px' }}
                        content={
                            <>
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                    <Grid item md={4}><MainSelectInput {...this.props} id='comdesconto' value={this.state.config.comdesconto || ''} optionsList={this.state.comissionDiscountOptions} label='Comissão Por Faixa' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={5}><MainCheckBoxInput {...this.props} id='comissaocompartilhada' value={this.state.config.comissaocompartilhada} label='Comissão Compartilhada' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainTextField required {...this.props} type='percent' id='desccooperado' value={this.state.config.desccooperado || ''} label='% Desconto Cooperado' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainTextField required {...this.props} type='percent' id='desclocal' value={this.state.config.desclocal || ''} label='% Desconto Local' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                    <Grid item md={4}><MainTextField required {...this.props} type='percent' id='deslimite' value={this.state.config.deslimite || ''} label='% Desconto Local Máximo' handleChange={this.handleChangeTextTabConfig} /></Grid>
                                </Grid>
                            </>
                        }
                    />

                    <MainTabButton sx={{ width: { xs: '100%', sm: '100%', md: '20%'}, marginLeft: '10px' }} {...this.props} onButtonClick={this.saveLocalSaleConfig} title="Salvar" />

                </Box>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.localSale, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabConfig = (event) => {
        handleChangeText(this.state.config, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabEmail = (event) => {
        handleChangeText(this.state.localSaleEmail, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeImage = (hexString, fieldName) => {
        handleChangeImage(this, this.state.localSale, hexString, fieldName, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            config: {},
            localSale: {},
            localSaleEmail: {},
            isLoadingLocalSaleEmailTable: true,
            isLoadingTab: true,
            isLoadingEmailInfo: true,
            newEmail: false
        })
    }

    onLocalSaleTableChange = (page) => {
        this.setState({ isLoadingLocalSaleTable: true })
        let config = {
            method: 'get',
            endpoint: 'localsale/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            status: this.state.status
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    localSaleList: r.data.local_sale,
                    localSaleColumns: r.data.columns,
                    localSaleTotalSize: r.data.total_size > 999 ? 999 : r.data.total_size,
                    isLoading: false,
                    isLoadingLocalSaleTable: false
                })
            }
        })
    }

    onLocalSaleEmailTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'localsale/email'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idlocalvenda
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    localSaleEmailList: r.data.local_sale_email,
                    localSaleEmailColumns: r.data.columns,
                    localSaleEmailTotalSize: r.data.total_size,
                    isLoadingLocalSaleEmailTable: false,
                    activeTab: 'emailConfig',
                }, () => this.handleChangeTab())
            }
        })
    }

    onLocalSaleEmailTableDoubleClick = (params) => {
        this.setState({
            localSaleEmail: params,
            isLoadingEmailInfo: false,
            newEmail: false
        }, () => this.handleChangeTab())
    }

    onLocalSaleEmailTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                localSaleEmailList: row // nova lista de e-mail semo que foi excluído
            }, () => this.deleteLocalSaleEmail(extraParam)) // extraParam = id da linha que foi excluída
        }
    }

    saveLocalSale = () => {
        let config = {
            method: 'post',
            endpoint: 'localsale/single'
        }
        let form = {
            localSale: this.state.localSale,
            id: this.state.localSale.idlocalvenda
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewLocalSale) {
                    newState['isANewLocalSale'] = false
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

    saveLocalSaleConfig = () => {
        let config = {
            method: 'post',
            endpoint: 'localsale/config/single'
        }
        let form = {
            config: this.state.config,
            id: this.state.localSale.idlocalvenda  //  id:  variável declarada aqui mesmo
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true
                })
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    saveLocalSaleEmail = () => {
        let config = {
            method: 'post',
            endpoint: 'localsale/email'
        }
        let form = {
            localSaleId: this.state.localSale.idlocalvenda,
            localSaleEmail: this.state.localSaleEmail,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    localSaleEmail: {},
                    isLoadingEmailInfo: true,
                    isLoadingLocalSaleEmailTable: true,

                    newEmail: false,

                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    searchLocalSaleInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'localsale/single'
        }
        let form = {
            id: this.state.selectedRow.idlocalvenda
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var localSaleConfig = r.data.config
                localSaleConfig.habilitarmargemvalor = localSaleConfig.habilitarmargemvalor === 'S'
                localSaleConfig.visualizarsaldoestoque = localSaleConfig.visualizarsaldoestoque === 'S'
                localSaleConfig.mostrabanner = localSaleConfig.mostrabanner === 'S'
                localSaleConfig.repetiritem = localSaleConfig.repetiritem === 'S'
                localSaleConfig.permitirvendabloqueado = localSaleConfig.permitirvendabloqueado === 'S'
                localSaleConfig.habilitareventosdesconto = localSaleConfig.habilitareventosdesconto === 'S'
                localSaleConfig.liberardescontovolume = localSaleConfig.liberardescontovolume === 'S'
                localSaleConfig.habilitardescontocliente = localSaleConfig.habilitardescontocliente === 'S'
                localSaleConfig.habilitardescontoadicional = localSaleConfig.habilitardescontoadicional === 'S'
                localSaleConfig.comissaocompartilhada = localSaleConfig.comissaocompartilhada === 'S'
                searchCEP(r.data.local_sale.cep).then((res) => {
                    var localSale = r.data.local_sale
                    localSale.cidade = res.city
                    this.setState({
                        config: localSaleConfig,
                        localSale: localSale,

                        isLoadingTab: false
                    }, () => this.handleChangeTab())
                }).catch((error) => {
                    this.setState({
                        config: localSaleConfig,
                        localSale: r.data.local_sale,

                        alertMessage: 'CEP não encontrado',
                        alertType: 'error',
                        showAlert: true,

                        isLoadingTab: false
                    }, () => this.handleChangeTab())
                })
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
                    <Header {...this.props} title='Locais de Venda' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '55% 15% 15% 15%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Pesquisar' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onLocalSaleTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.setState({ isANewLocalSale: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>
                        <EditableTable
                            {...this.props}
                            id='localsaleTable'
                            allowEdit
                            noDeleteButton
                            data={this.state.localSaleList}
                            columns={this.state.localSaleColumns}
                            rowId={'idlocalvenda'}
                            totalSize={this.state.localSaleTotalSize}
                            onPageChange={this.onLocalSaleTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingLocalSaleTable}
                            extraColumnsConfig={
                                {
                                    'idlocalvenda': {
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

export default LocalSale;