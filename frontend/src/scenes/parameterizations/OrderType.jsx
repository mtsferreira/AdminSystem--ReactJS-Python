import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import LoadingGif from "../../components/visual/LoadingGif";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class OrderType extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            isLoading: true,
            isLoadingTab: true,
            isLoadingOrderTypeTable: true,
            menuId: '38',

            orderType: {},
            orderTypeList: [],
            orderTypeColumns: {},
            orderTypeTotalSize: '',

            printLayoutOptions: [
                { 'value': 'R', 'label': 'Retrato' },
                { 'value': 'P', 'label': 'Paisagem' },
            ],
            printOrderOptions: [
                { 'value': 'E', 'label': 'Lançamento' },
                { 'value': 'S', 'label': 'SKU' },
                { 'value': 'D', 'label': 'Descrição' },
            ],
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'C', 'label': 'Cancelado' },
            ],

            isANewOrderType: false,
            search: '',
            status: 'A',
            activeTab: 'data',
            tabs: [
                { id: 'data', title: 'Dados' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onOrderTypeTableChange(0)
        optionsRequest(this, ['priceRules', 'shippingCif', 'margin', 'cascade'])
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onOrderTypeTableChange(0)
    }

    createEditTab = (params, isRegister = false) => {
        this.setState({
            isANewOrderType: isRegister ? true : false,
            selectedRow: params,
            isLoadingTab: isRegister ? false : true,
            orderType: {
                temmargem: false,
                temminimo: false,
                alterarvalorfrete: false,
                temestoque: false,
                temvolume: false,
                temcascata: false,
            }
        }, () => createEditTab(isRegister ? 'Cadastro de tipo de pedido' : 'Alteração de tipo de pedido', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab && !this.state.isANewOrderType) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchOrderTypeInfo())
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid 
                        container 
                        columnSpacing={1} 
                        rowSpacing={2}
                        sx={{
                            flexDirection: { xs: 'column', sm: 'column', md: 'row' },
                            margin: '15px 0',
                        }}
                    >
                        <Grid item md={2}><MainTextField required {...this.props} type='number' id='coderp' value={this.state.orderType.coderp || ''} label='Código ERP' handleChange={this.handleChangeTextTab} disabled={!this.state.isANewOrderType ? true : false} fullWidth /></Grid>
                        <Grid item md={8}><MainTextField required {...this.props} id='destipopedido' value={this.state.orderType.destipopedido || ''} label='Descrição' handleChange={this.handleChangeTextTab} disabled={!this.state.isANewOrderType ? true : false} fullWidth /></Grid>
                        <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.orderType.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} /></Grid>

                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="" /></Grid>


                        <Grid Grid item md={10}>
                            <Grid container columnSpacing={1} rowSpacing={2} sx={{
                            flexDirection: { xs: 'column', sm: 'column', md: 'row' },
                            margin: '15px 0',
                        }}>
                                <Grid item md={6}><MainSelectInput {...this.props} id='ordemimpressao' value={this.state.orderType.ordemimpressao || ''} optionsList={this.state.printOrderOptions} label='Ordem Impressão dos Itens' handleChange={this.handleChangeTextTab} /></Grid>
                                <Grid item md={6}><MainSelectInput {...this.props} id='layoutimpressao' value={this.state.orderType.layoutimpressao || ''} optionsList={this.state.printLayoutOptions} label='Layout de Impressão' handleChange={this.handleChangeTextTab} /></Grid>

                                <Grid item md={6}><MainCheckBoxInput {...this.props} id='temmargem' value={this.state.orderType.temmargem} label='Calcular margem de contribuição' handleChange={this.handleChangeTextTab} /></Grid>
                                <Grid item md={6}><MainCheckBoxInput {...this.props} id='temminimo' value={this.state.orderType.temminimo} label='Controlar quantidade mínima do pedido' handleChange={this.handleChangeTextTab} /></Grid>
                                <Grid item md={6}><MainCheckBoxInput {...this.props} id='alterarvalorfrete' value={this.state.orderType.alterarvalorfrete} label='Permitir alterar valor do frete' handleChange={this.handleChangeTextTab} /></Grid>
                                <Grid item md={6}><MainCheckBoxInput {...this.props} id='temestoque' value={this.state.orderType.temestoque} label='Controlar estoque do produto no pedido' handleChange={this.handleChangeTextTab} /></Grid>
                            </Grid>
                        </Grid>

                        <Grid Grid item md={2}>
                            <Box sx={{ border: '2px solid', borderColor: this.props.colors.grey[1100], borderRadius: '5px', padding: '0 15px', height: '100%', width: '93%' }}>
                                <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Desconto" /></Grid>
                                <Grid item md={2} sx={{ marginTop: '5px' }}><MainCheckBoxInput {...this.props} id='temvolume' value={this.state.orderType.temvolume} label='Volume' handleChange={this.handleChangeTextTab} /></Grid>
                                <Grid item md={2} sx={{ marginTop: '15px' }}><MainCheckBoxInput {...this.props} id='temcascata' value={this.state.orderType.temcascata} label='Cascata' handleChange={this.handleChangeTextTab} /></Grid>
                            </Box>
                        </Grid>

                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="" /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} id='idpreco' value={this.state.orderType.idpreco || ''} optionsList={this.state.priceRulesOptions} label='Regra de Preço' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput {...this.props} id='idmargem' value={this.state.orderType.idmargem || ''} optionsList={this.state.marginOptions} label='Tipo de Margem de Contribuição' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput required {...this.props} id='idfretecif' value={this.state.orderType.idfretecif || ''} optionsList={this.state.shippingCifOptions} label='Frete CIF' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput required {...this.props} id='desccomposto' value={this.state.orderType.desccomposto || ''} optionsList={this.state.cascadeOptions} label='Desconto Comercial' handleChange={this.handleChangeTextTab} fullWidth /></Grid>

                        <Grid item md={2}>
                            <MainTabButton sx={{width: { sm: '97%', md: '94%'}}} {...this.props} onButtonClick={this.saveOrderType} title="Salvar" />
                        </Grid>
                    </Grid>
                </Box>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.orderType, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            orderType: {},
            isLoadingTab: true,
        })
    }

    onOrderTypeTableChange = (page) => {
        this.setState({
            isLoadingproductRegisteTable: true
        })
        let config = {
            method: 'get',
            endpoint: 'order/type/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            status: this.state.status
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    orderTypeList: r.data.order_type,
                    orderTypeColumns: r.data.columns,
                    orderTypeTotalSize: r.data.total_size,
                    isLoading: false,
                    isLoadingOrderTypeTable: false,
                })
            }
        })
    }

    saveOrderType = () => {
        let config = {
            method: 'post',
            endpoint: 'order/type/single'
        }
        let form = {
            id: this.state.orderType.idtipopedido,
            orderType: this.state.orderType,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewOrderType) {
                    newState['isANewOrderType'] = false
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

    searchOrderTypeInfo = () => {
        if (this.state.isANewOrderType) {
            this.setState({ isLoadingTab: false })
            return
        }
        let config = {
            method: 'get',
            endpoint: 'order/type/single'
        }
        let form = {
            id: this.state.selectedRow.idtipopedido
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var orderType = r.data.order_type
                orderType.temvolume = orderType.temvolume === 'S'
                orderType.temcascata = orderType.temcascata === 'S'
                orderType.temmargem = orderType.temmargem === 'S'
                orderType.temminimo = orderType.temminimo === 'S'
                orderType.temestoque = orderType.temestoque === 'S'
                orderType.alterarvalorfrete = orderType.alterarvalorfrete === 'S'

                this.setState({
                    orderType: r.data.order_type,
                    isLoadingTab: false
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
                    <Header {...this.props} title='Tipo de Pedido' menuId={this.state.menuId} showFav />
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
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => { this.setState({ isLoadingOrderTypeTable: true }, () => this.onOrderTypeTableChange(0)) }}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.setState({ isANewOrderType: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>
                        <EditableTable
                            {...this.props}
                            allowEdit
                            noDeleteButton
                            id='ordertypeTable'
                            data={this.state.orderTypeList}
                            columns={this.state.orderTypeColumns}
                            rowId={'idtipopedido'}
                            totalSize={this.state.orderTypeTotalSize}
                            onPageChange={this.onOrderTypeTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingOrderTypeTable}
                            extraColumnsConfig={
                                {
                                    'coderp': {
                                        'type': 'number',
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
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

export default OrderType;