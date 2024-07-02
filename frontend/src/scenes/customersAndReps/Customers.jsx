import React from "react";
import ReactDOM from "react-dom";

import Accordion from "../../components/visual/Accordion";
import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import LoadingGif from "../../components/visual/LoadingGif";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainDateTimeInput from "../../components/inputs/MainDateTimeInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

// Icons
import SearchIcon from '@mui/icons-material/Search';

import { Box, Button, IconButton, Grid, Typography } from "@mui/material";
import { addLastAccess, changeActiveTabStyle, createEditTab } from "../../utils/layout";
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";
import { searchCEP } from "../../utils/request/apiRequest";


class Customers extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            menuId: '4',
            isLoading: true,
            isLoadingTab: true,
            isLoadingCustomersTable: true,
            isLoadingCustomersAddressTable: true,
            isLoadingCustomersContactTable: true,
            isLoadingCustomerSellerTable: true,
            isLoadingCustomerSellerInfos: true,

            search: '',
            status: '',
            corporateReason: '',
            newCustomerSeller: false,
            selectedUser: null,

            customer: {},
            customerSeller: {},

            customerList: [],
            customerColumns: [],
            customerTotalSize: '',

            customerAddressList: [],
            customerAddressColumns: [],
            customerAddressTotalSize: '',

            customerContactList: [],
            customerContactColumns: [],
            customerContactTotalSize: '',

            customerSellerList: [],
            customerSellerColumns: [],
            customerSellerTotalSize: '',

            activeTab: 'basicInfos',
            tabs: [
                { id: 'basicInfos', title: 'Informações' },
                { id: 'fiscalData', title: 'Dados Fiscais' },
                { id: 'address', title: 'Endereços' },
                { id: 'profile', title: 'Perfil e Política' },
                { id: 'customersAndSellers', title: 'Cliente X Vendedores' },
                { id: 'contacts', title: 'Contatos' }
            ],

            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'C', 'label': 'Cancelado' },
                { 'value': 'S', 'label': 'Suspenso' }
            ],

            comercialDiscountOptions: [],
            customerTypeOptions: [],
            destinationOptions: [],
            economicGroupOptions: [],
            fiscalStatusOptions: [],
            legalNatureOptions: [],
            networkOptions: [],
            orderTypeOptions: [],
            rulesPriceOptions: [],
            sellignAreaOptions: [],
            shippingTypeOptions: [],
            shippingOptions: [],
            userOptions: [],
            volumeDiscountOptions: []
        }

        this.customerSellerRef = React.createRef()
    }

    componentDidMount() {
        this.onCustomersTableChange(0)
        addLastAccess(this.state.menuId)
    }

    componentDidUpdate() {
        if (this.customerSellerRef.current) {
            this.customerSellerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
    }

    clearAllFields = (e) => {
        this.setState({
            erp: '',
            document: '',
            search: ''
        })
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
        }, () => createEditTab('Informações do Cliente', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    customerSellerEdit = (params) => {
        let config = {
            method: 'get',
            endpoint: 'customer/seller/single'
        }

        let form = {
            id: this.state.customer.idcliente,
            customerSellerId: params.idclientevendedor
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var customerSeller = r.data.customer_seller
                customerSeller.visit.seg = customerSeller.visit.seg === 'S'
                customerSeller.visit.ter = customerSeller.visit.ter === 'S'
                customerSeller.visit.qua = customerSeller.visit.qua === 'S'
                customerSeller.visit.qui = customerSeller.visit.qui === 'S'
                customerSeller.visit.sex = customerSeller.visit.sex === 'S'
                customerSeller.visit.sab = customerSeller.visit.sab === 'S'
                customerSeller.visit.dom = customerSeller.visit.dom === 'S'

                this.setState({
                    customerSeller: customerSeller,
                    isLoadingCustomerSellerInfos: false,
                    newCustomerSeller: false,

                }, () => this.handleChangeTab())

            }
        })
    }

    editSellerCustomer = () => {
        if (this.state.newCustomerSeller && !this.state.selectedUser) {
            this.setState({
                alertType: 'error',
                alertMessage: 'Preencha todos os campos obrigatorios (*)',
                showAlert: true,
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'customer/seller/single'
        }
        let form = {
            id: this.state.customer.idcliente,
            customerSellerId: this.state.customerSeller.idclientevendedor,
            customerSeller: this.state.customerSeller
        }

        if (this.state.newCustomerSeller) {
            form['userId'] = this.state.selectedUser
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    isLoadingCustomerSellerInfos: true,
                    customerSeller: null,
                    newCustomerSeller: false,
                }, () => {
                    this.onCustomerSellerTableChange(0, () => this.handleChangeTab())
                })
            } else {
                this.setState({
                    alertType: 'error',
                    alertMessage: r.data.message,
                    showAlert: true,
                })
            }
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchCustomerInfo())
            return
        }
        if (!this.state.customer) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'basicInfos') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={3}><MainTextField {...this.props} type='number' disabled id='coderp' value={this.state.customer.coderp || ''} label='Código ERP' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} type='number' disabled id='cnpjcpf' value={this.state.customer.cnpjcpf || ''} label='CNPJ/CPF' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} disabled id='situacao' value={this.state.customer.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '94%' }} /></Grid>
                        <Grid item md={12}><MainTextField {...this.props} disabled id='razao' value={this.state.customer.razao || ''} label='Razão Social' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={12}><MainTextField {...this.props} disabled id='fantasia' value={this.state.customer.fantasia || ''} label='Fantasia' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} disabled id='ufcliente' value={this.state.customer.ufcliente || ''} label='Inscrição Estadual' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} disabled id='dados.datafundacao' value={this.state.customer.dados.datafundacao || ''} label='Data Fundação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>

                        {/* Address info */}
                        <Grid item md={12}>
                            <Accordion
                                {...this.props}
                                title='Endereço'
                                customCss={{ width: '97%' }}
                                content={
                                    <>
                                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                            <Grid item md={3}><MainTextField {...this.props} type='number' disabled id='dados.cep' value={this.state.customer.dados.cep || ''} label='CEP' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={5}><MainTextField {...this.props} disabled id='dados.logradouro' value={this.state.customer.dados.logradouro || ''} label='Logradouro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={4}><MainTextField {...this.props} disabled id='dados.bairro' value={this.state.customer.dados.bairro || ''} label='Bairro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={3}><MainTextField {...this.props} type='number' disabled id='dados.numero' value={this.state.customer.dados.numero || ''} label='Número' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={3}><MainTextField {...this.props} disabled id='dados.complemento' value={this.state.customer.dados.complemento || ''} label='Complemento' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={4}><MainTextField {...this.props} disabled id='dados.cidade' value={this.state.customer.dados.cidade || ''} label='Cidade' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={2}><MainTextField {...this.props} disabled id='dados.uf' value={this.state.customer.dados.uf || ''} label='UF' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '94%' }}  /></Grid>
                                        </Grid>
                                    </>
                                }
                            />
                        </Grid>

                        {/* Personal info */}
                        <Grid item md={12}>
                            <Accordion
                                {...this.props}
                                title='Contatos'
                                customCss={{ width: '97%' }}
                                content={
                                    <>
                                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                            <Grid item md={6}><MainTextField {...this.props} disabled id='dados.email' value={this.state.customer.dados.email || ''} label='Email' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={3}><MainTextField {...this.props} disabled id='dados.telfixo' value={this.state.customer.dados.telfixo || ''} label='Telefone Fixo' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={3}><MainTextField {...this.props} disabled id='dados.telcelular' value={this.state.customer.dados.telcelular || ''} label='Telefone Celular' handleChange={this.handleChangeTextTab} width={'97%'} /></Grid>
                                        </Grid>
                                    </>
                                }
                            />
                        </Grid>

                        {/* Synced User */}
                        <Grid item md={12}>
                            <Accordion
                                {...this.props}
                                title='Usuário Vinculado'
                                customCss={{ width: '97%' }}
                                content={
                                    <>
                                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                            <Grid item md={3}><MainTextField {...this.props} disabled id='erpuser' value={this.state.erpuser || ''} label='Usuário ERP' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                            <Grid item md={9}><MainTextField {...this.props} disabled id='userName' value={this.state.userName || ''} label='Nome do Usuário' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        </Grid>
                                    </>
                                }
                            />
                        </Grid>
                    </Grid>
                </Box>
        } else if (page === 'fiscalData') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={3}><MainTextField {...this.props} disabled id='fiscal.cnaeprincipal' value={this.state.customer.fiscal.cnaeprincipal || ''} label='CNA Principal' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} disabled id='fiscal.inscestadual' value={this.state.customer.fiscal.inscestadual || ''} label='Inscrição Estadual' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} disabled id='fiscal.inscmunicipal' value={this.state.customer.fiscal.inscmunicipal || ''} label='Inscrição Municipal' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainSelectInput {...this.props} disabled id='fiscal.sitfiscal' value={this.state.customer.fiscal.sitfiscal} optionsList={this.state.fiscalStatusOptions} label='Situação Fiscal' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={12}><MainSelectInput {...this.props} disabled id='fiscal.natjuridica' value={this.state.customer.fiscal.natjuridica} optionsList={this.state.legalNatureOptions} label='Natureza Jurídica' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} disabled id='fiscal.destinacao' value={this.state.customer.fiscal.destinacao} optionsList={this.state.destinationOptions} label='Destinação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={4}><MainCheckBoxInput {...this.props} disabled id='fiscal.contribuinteicms' value={this.state.customer.fiscal.contribuinteicms} label='Contribuinte ICMS' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={4}><MainCheckBoxInput {...this.props} disabled id='fiscal.orgaopublico' value={this.state.customer.fiscal.orgaopublico} label='Órgão Público' handleChange={this.handleChangeTextTab} /></Grid>
                        {/*  */}
                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Tipo de Regime Especial" /></Grid>
                        <Accordion
                            {...this.props}
                            title='SUFRAMA'
                            customCss={{ margin: '0 10px 20px 7px' }}
                            content={
                                <>
                                    <Grid container spacing={1} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                        <Grid item md={4}><MainTextField {...this.props} type='number' disabled id='especial.regsuframa' value={this.state.customer.especial.regsuframa} label='Número de Registro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        <Grid item md={4}><MainTextField {...this.props} disabled id='especial.dataregsuframa' value={this.state.customer.especial.dataregsuframa} label='Data de Registro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        <Grid item md={4}><MainTextField {...this.props} disabled id='especial.datavalsuframa' value={this.state.customer.especial.datavalsuframa} label='Data de Validade' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                    </Grid>
                                </>
                            }
                        />
                        <Accordion
                            {...this.props}
                            title='TARE'
                            customCss={{ margin: '0 10px 20px 7px' }}
                            content={
                                <>
                                    <Grid container spacing={1}>
                                        <Grid item md={4}><MainTextField {...this.props} type='number' disabled id='especial.regtare' value={this.state.customer.especial.regtare} label='Número de Registro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        <Grid item md={4}><MainTextField {...this.props} disabled id='especial.dataregtare' value={this.state.customer.especial.dataregtare} label='Data de Registro' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        <Grid item md={4}><MainTextField {...this.props} disabled id='especial.datavaltare' value={this.state.customer.especial.datavaltare} label='Data de Validade' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                    </Grid>
                                </>
                            }
                        />
                        <Accordion
                            {...this.props}
                            title='NOTA'
                            customCss={{ margin: '0 10px 20px 7px' }}
                            content={
                                <>
                                    <Grid container spacing={1}>
                                        <Grid item md={3}><MainTextField {...this.props} disabled id='especial.carimbo' value={this.state.customer.especial.carimbo} label='Carimbo na Nota' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                                        <Grid item md={9}></Grid>
                                        <Grid item md={6}><MainTextField {...this.props} disabled id='especial.descricao_carimbo' value={this.state.customer.especial.descricao_carimbo} label='Descrição Carimbo' handleChange={this.handleChangeTextTab} minRows={5} fullWidth /></Grid>
                                        <Grid item md={6}><MainTextField {...this.props} disabled id='especial.descricaocarimbo' value={this.state.customer.especial.descricaocarimbo} label='Descrição Adicional do Carimbo' handleChange={this.handleChangeTextTab} minRows={5} fullWidth /></Grid>
                                    </Grid>
                                </>
                            }
                        />
                    </Grid>
                </Box>
        } else if (page === 'address') {
            if (this.state.isLoadingCustomersAddressTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onCustomerAddressTableChange(0))
                return
            }
            context =
                <EditableTable
                    {...this.props}
                    id='addressTable'
                    height='40vh'
                    data={this.state.customerAddressList}
                    columns={this.state.customerAddressColumns}
                    totalSize={this.state.customerAddressTotalSize}
                    rowId={'idendereco'}
                    onPageChange={this.onCustomerAddressTableChange}
                    onEditRow={this.onCustomerAddressTableEdit}
                    onRowDoubleClick={() => { }}
                    isLoading={this.state.isLoadingCustomersAddressTable}
                />
        } else if (page === 'profile') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={6}><MainSelectInput {...this.props} disabled id='perfil.tipocliente' value={this.state.customer.perfil.tipocliente} optionsList={this.state.customerTypeOptions} label='Tipo de Cliente' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} disabled id='perfil.idtipopedido' value={this.state.customer.perfil.idtipopedido} optionsList={this.state.orderTypeOptions} label='Tipo de Pedido' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} disabled id='perfil.grupoeco' value={this.state.customer.perfil.grupoeco} optionsList={this.state.economicGroupOptions} label='Grupo Econômico' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} disabled id='perfil.rede' value={this.state.customer.perfil.rede} optionsList={this.state.networkOptions} label='Rede (Marca)' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} disabled id='perfil.descomposto' value={this.state.customer.perfil.descomposto || ''} label='Desconto Composto' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} type='percent' disabled id='perfil.perdesconto' value={this.state.customer.perfil.perdesconto || ''} label='Desconto (%)' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '94%' }} /></Grid>
                        <Grid item md={3}><MainTextField {...this.props} type='number' disabled id='perfil.prazomedio' value={this.state.customer.perfil.prazomedio || ''} label='Prazo Médio' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainSelectInput {...this.props} disabled id='perfil.tipofrete' value={this.state.customer.perfil.tipofrete} optionsList={this.state.shippingTypeOptions} label='Tipo de Frete' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '94%' }} /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} id='perfil.idprecoregra' value={this.state.customer.perfil.idprecoregra} optionsList={this.state.rulesPriceOptions} label='Regra de Formação de Preço' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} id='perfil.idregiao' value={this.state.customer.perfil.idregiao} optionsList={this.state.sellignAreaOptions} label='Região de Vendas' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                        <Grid item md={12}><MainSelectInput {...this.props} id='perfil.idtransportador' value={this.state.customer.perfil.idtransportador} optionsList={this.state.shippingOptions} label='Transportador Acordado' handleChange={this.handleChangeTextTab} width='98.5%' /></Grid>
                        <Grid item md={12}><MainTextField {...this.props} id='perfil.descgeral' value={this.state.customer.perfil.descgeral || ''} label='Descrição Geral' handleChange={this.handleChangeTextTab} width='98.5%' /></Grid>

                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Condições Especiais" /></Grid>
                        <Grid item md={3}><MainSelectInput required {...this.props} id='perfil.limitecredito' value={this.state.customer.perfil.limitecredito} optionsList={this.state.statusOptions} label='Limite de Crédito' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={6}><MainCheckBoxInput {...this.props} id='perfil.pedidominimo' value={this.state.customer.perfil.pedidominimo} label='Exige Pedido Mínimo' handleChange={this.handleChangeTextTab} /></Grid>

                        <Grid item md={3}>
                            <MainTabButton width='94%' {...this.props} onButtonClick={this.saveCustomerProfile} title="Salvar" />
                        </Grid>
                    </Grid>
                </Box>
        } else if (page === 'customersAndSellers') {
            if (this.state.isLoadingCustomerSellerTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onCustomerSellerTableChange(0, this.handleChangeTab))
                return
            }
            context =
                <>
                    <MainTabButton
                        sx={{ width: { xs: '100%', sm: '100%', md: '20%'}, marginTop: '15px' }}
                        {...this.props}
                        onButtonClick={() => {
                            this.setState({
                                customerSeller: {
                                    visit: {
                                        seg: false,
                                        ter: false,
                                        qua: false,
                                        qui: false,
                                        sex: false,
                                        sab: false,
                                        dom: false,
                                    }
                                },
                                selectedUser: null,
                                isLoadingCustomerSellerInfos: false,
                                newCustomerSeller: true,
                            }, () => this.handleChangeTab())
                        }}
                        title="Adicionar Novo"
                    />


                    <EditableTable
                        {...this.props}
                        customMargin='10px 0 0 0'
                        id='sellerTable'
                        allowEdit
                        height='40vh'
                        data={this.state.customerSellerList}
                        columns={this.state.customerSellerColumns}
                        totalSize={this.state.customerSellerTotalSize}
                        rowId={'idclientevendedor'}
                        onPageChange={this.onCustomerSellerTableChange}
                        onEditRow={this.onCustomerSellerTableEdit}
                        onRowDoubleClick={this.customerSellerEdit}
                        isLoading={this.state.isLoadingCustomerSellerTable}
                    />
                    <div id='visitCalendarDiv'>
                        {!this.state.isLoadingCustomerSellerInfos ?
                            <>
                                <Box sx={{ flexGrow: 1 }} ref={this.customerSellerRef}>
                                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0 0 0' }}>
                                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Calendário de Visitas" /></Grid>
                                        {this.state.newCustomerSeller ?
                                            <Grid item md={12}><MainSelectInput required {...this.props} id='idcascata' value={this.state.selectedUser || null} optionsList={this.state.userOptions} label='Vendedor' handleChange={(event) => this.setState({ selectedUser: event.target.value }, () => this.handleChangeTab())} width='99.5%' /></Grid>
                                            : <></>}
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.seg' value={this.state.customerSeller.visit?.seg || false} label='Segunda' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.ter' value={this.state.customerSeller.visit?.ter || false} label='Terça' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.qua' value={this.state.customerSeller.visit?.qua || false} label='Quarta' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.qui' value={this.state.customerSeller.visit?.qui || false} label='Quinta' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.sex' value={this.state.customerSeller.visit?.sex || false} label='Sexta' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={2}><MainCheckBoxInput {...this.props} id='visit.sab' value={this.state.customerSeller.visit?.sab || false} label='Sábado' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={6}><MainCheckBoxInput {...this.props} id='visit.dom' value={this.state.customerSeller.visit?.dom || false} label='Domingo' handleChange={this.handleChangeTextSeller} /></Grid>
                                        <Grid item md={3}><MainDateTimeInput {...this.props} id='visit.hora1' value={this.state.customerSeller.visit?.hora1 || ''} label='Hora Abertura' handleChange={this.handleChangeTextSeller} type='time' fullWidth /></Grid>
                                        <Grid item md={3}><MainDateTimeInput {...this.props} id='visit.hora2' value={this.state.customerSeller.visit?.hora2 || ''} label='Hora Fechamento' handleChange={this.handleChangeTextSeller} type='time' fullWidth /></Grid>
                                        <Grid item md={6}><MainSelectInput required {...this.props} id='idcascata' value={this.state.customerSeller.idcascata || null} optionsList={this.state.comercialDiscountOptions} label='Desconto Comercial' handleChange={this.handleChangeTextSeller} fullWidth /></Grid>
                                        <Grid item md={6}><MainSelectInput required {...this.props} id='idvolume' value={this.state.customerSeller.idvolume || null} optionsList={this.state.volumeDiscountOptions} label='Desconto por Volume' handleChange={this.handleChangeTextSeller} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>
                                    </Grid>
                                </Box>
                            
                                <MainTabButton sx={{ width: '20%', margin: '15px 0 0 7px' }} {...this.props} onButtonClick={this.editSellerCustomer} title="Salvar" />

                            </>
                            :
                            <>
                            </>
                        }
                    </div>
                </>
        } else if (page === 'contacts') {
            if (this.state.isLoadingCustomersContactTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onCustomerContactTableChange(0))
                return
            }
            context =
                <EditableTable
                    {...this.props}
                    id='contactTable'
                    allowEdit
                    allowEditOnRow
                    noDeleteButton
                    height='70vh'
                    data={this.state.customerContactList}
                    columns={this.state.customerContactColumns}
                    totalSize={this.state.customerContactTotalSize}
                    rowId={'idcontato'}
                    onPageChange={this.onCustomerContactTableChange}
                    onEditRow={this.onCustomerContactTableEdit}
                    onRowDoubleClick={() => { }}
                    isLoading={this.state.isLoadingCustomersContactTable}
                    extraColumnsConfig={
                        {
                            'datanascimento': {
                                'type': 'date'
                            },
                            'situacao': {
                                'type': 'select',
                                'options': [
                                    { value: 'A', label: 'Ativo' },
                                    { value: 'X', label: 'Inativo' },
                                ]
                            },
                            'telfixo': {
                                'type': 'number',
                            },
                            'telcelular': {
                                'type': 'number',
                            },
                            'numwhats': {
                                'type': 'number',
                            },
                            'idcontato': {
                                'disabled': true,
                                'type': 'number'
                            }
                        }
                    }
                />
        }

        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        var componentThis = this

        document.getElementById(event.target.id).addEventListener('keyup', function onEvent(e) {
            if (e.key === 'Enter') {
                componentThis.setState({
                    isLoadingCustomersTable: true
                }, () => componentThis.onCustomersTableChange(0))
                return
            }
        })

        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.customer, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextSeller = (event) => {
        handleChangeText(this.state.customerSeller, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            customer: {},
            customerSeller: {},
            isLoadingTab: true,
            isLoadingCustomerSellerInfos: true,
            isLoadingCustomerSellerTable: true,
            isLoadingCustomersAddressTable: true,
            isLoadingCustomersContactTable: true,
            activeTab: 'basicInfos'
        })
    }

    onCustomersTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'customer/search'
        }

        let form = {
            page: page,
            term: this.state.search
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerList: r.data.customers,
                    customerColumns: r.data.columns,
                    customerTotalSize: r.data.total_size > 999 ? 999 : r.data.total_size,
                    isLoading: false,
                    isLoadingCustomersTable: false
                })
            }
        })
    }

    onCustomersTableEdit = (row, method, extraParam) => {
        if (method === 'add') {
            this.setState({
                customerContactList: [row, ...this.state.customerContactList]
            }, () => this.handleChangeTab())
        } else if (method === 'delete') {
            this.setState({
                customerContactList: row
            }, () => this.deleteTableRow('customer', 'customer', extraParam))
        }
    }

    onCustomerAddressTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'customer/address'
        }

        let form = {
            id: this.state.customer.idcliente,
            page: page
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerAddressList: r.data.address,
                    customerAddressColumns: r.data.columns,
                    customerAddressTotalSize: r.data.total_size,
                    isLoadingCustomersAddressTable: false,
                    activeTab: 'address'
                }, () => this.handleChangeTab())
            }
        })
    }

    onCustomerAddressTableEdit = (row, method, extraParam) => {
        if (method === 'add') {
            this.setState({
                customerAddressList: [row, ...this.state.customerAddressList]
            }, () => this.handleChangeTab())
        } else if (method === 'delete') {
            this.setState({
                customerAddressList: row
            }, () => this.deleteTableRow('customer/address', 'address', extraParam))
        } else if (method === 'edit') {
            this.setState({
                customerAddressList: row
            }, () => this.editTableRow('customer/address', 'address', extraParam))
        }
    }

    onCustomerContactTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'customer/contact'
        }

        let form = {
            id: this.state.customer.idcliente,
            page: page
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerContactList: r.data.contact,
                    customerContactColumns: r.data.columns,
                    customerContactTotalSize: r.data.total_size,
                    isLoadingCustomersContactTable: false,
                    activeTab: 'contacts'
                }, () => this.handleChangeTab())
            }
        })
    }

    onCustomerContactTableEdit = (row, method, extraParam) => {
        if (method === 'add') {
            this.setState({
                customerContactList: [row, ...this.state.customerContactList]
            }, () => this.handleChangeTab())
        } else if (method === 'delete') {
            this.setState({
                customerContactList: row
            }, () => this.deleteTableRow('customer/contact', 'contact', extraParam))
        } else if (method === 'edit') {
            this.setState({
                customerContactList: row
            }, () => this.editTableRow('customer/contact', 'contact', extraParam))
        }
    }

    onCustomerSellerTableChange = (page, callback = null) => {
        let config = {
            method: 'get',
            endpoint: 'customer/seller'
        }

        let form = {
            id: this.state.customer.idcliente,
            page: page
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerSellerList: r.data.seller,
                    customerSellerColumns: r.data.columns,
                    customerSellerTotalSize: r.data.total_size,
                    isLoadingCustomerSellerTable: false,
                    activeTab: 'customersAndSellers'
                }, callback)
            }
        })
    }

    onCustomerSellerTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                customerSellerList: row
            }, () => this.deleteTableRow('customer/seller/single', 'customerSeller', extraParam))
        }
    }

    deleteTableRow = (endpoint, origin, contactId) => {
        let config = {
            method: 'delete',
            endpoint: endpoint
        }

        let form = {
            id: this.state.customer.idcliente,
            [origin + 'Id']: contactId
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    isLoadingCustomerSellerInfos: true
                }, () => this.handleChangeTab())
            }
        })
    }

    editTableRow = (endpoint, origin, infos) => {
        let config = {
            method: 'post',
            endpoint: endpoint
        }

        let form = {
            id: this.state.customer.idcliente,
            [origin]: infos
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.handleChangeTab()
            }
        })
    }

    saveCustomerProfile = () => {
        let config = {
            method: 'post',
            endpoint: 'customer/profile'
        }
        let form = {
            id: this.state.selectedRow.idcliente,
            profile: this.state.customer.perfil
        }
        defaultRequest(config, form).then((r) => {
            this.setState({
                alertType: r.status ? 'success' : 'error',
                alertMessage: r.data.message,
                showAlert: true,
            })
        })
    }

    searchCustomerInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'customer'
        }

        let form = {
            id: this.state.selectedRow.idcliente
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                searchCEP(r.data.customer.dados.cep).then((res) => {
                    const cityUF = res

                    r.data.customer.dados.cidade = cityUF.city
                    r.data.customer.dados.uf = cityUF.uf
                    r.data.customer.fiscal.contribuinteicms = r.data.customer.fiscal.contribuinteicms === 'S'
                    r.data.customer.fiscal.orgaopublico = r.data.customer.fiscal.orgaopublico === 'S'
                    r.data.customer.perfil.pedidominimo = r.data.customer.perfil.pedidominimo === 'S'

                    this.setState({
                        customer: r.data.customer,
                        isLoadingTab: false,

                        destinationOptions: r.data.options_destination,
                        comercialDiscountOptions: r.data.comercial_discount_options,
                        customerTypeOptions: r.data.options_customer_type,
                        economicGroupOptions: r.data.options_economic_group,
                        fiscalStatusOptions: r.data.options_fiscal_status,
                        legalNatureOptions: r.data.options_legal_nature,
                        networkOptions: r.data.options_network,
                        orderTypeOptions: r.data.options_order_type,
                        rulesPriceOptions: r.data.options_rules_price,
                        sellignAreaOptions: r.data.options_selling_area,
                        shippingTypeOptions: r.data.options_shipping_type,
                        shippingOptions: r.data.options_shipping,
                        userOptions: r.data.user_options,
                        volumeDiscountOptions: r.data.volume_discount_options,
                    }, () => this.handleChangeTab())
                }).catch((error) => {
                    // POPAR O ERRO DE CEP MAS ABRIR A TELA
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
                    <Header {...this.props} title='Clientes' menuId={this.state.menuId} showFav />

                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '15px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '80% 20%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Pesquisar' inputProps={<IconButton onClick={() => this.setState({ isLoadingCustomersTable: true }, this.onCustomersTableChange(0))}><SearchIcon /></IconButton>} handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={this.clearAllFields}>Limpar</Button>
                        </Box>
                        <EditableTable
                            {...this.props}
                            id='customerTable'
                            allowEdit
                            noDeleteButton
                            data={this.state.customerList}
                            columns={this.state.customerColumns}
                            rowId={'idcliente'}
                            totalSize={this.state.customerTotalSize}
                            onPageChange={this.onCustomersTableChange}
                            onEditRow={this.onCustomersTableEdit}
                            onRowDoubleClick={this.createEditTab}
                            isLoading={this.state.isLoadingCustomersTable}
                            extraColumnsConfig={
                                {
                                    'idcliente': {
                                        'type': 'number'
                                    },
                                    'coderp': {
                                        'type': 'number'
                                    }
                                }
                            }
                        />
                    </Box>
                </Box>
            </>
        )
    }
}

export default Customers