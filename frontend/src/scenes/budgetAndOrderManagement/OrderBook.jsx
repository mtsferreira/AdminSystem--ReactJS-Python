import React from "react";
import ReactDOM from "react-dom";

import Accordion from "../../components/visual/Accordion";
import EditableTable from "../../components/tables/EditableTable";
import dayjs from "dayjs";
import Header from "../../components/Header";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainDateTimeInput from "../../components/inputs/MainDateTimeInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class OrderBook extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingOptions: true,
            isLoadingOrderBookTable: true,

            menuId: '12',

            localSale: null,
            client: null,
            seller: null,
            orderNumber: null,

            initialDate: dayjs('2023-01-01').format('YYYY-MM-DD'),
            finalDate: dayjs().format('YYYY-MM-DD'),

            situation: {
                inPreparation: false,
                salesOrder: false,
                invoiced: false,
                canceled: false,
            },

            orderBook: {},
            orderBookList: [],
            orderBookColumns: {},
            orderBookTotalSize: '',

            danfeStatusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'C', 'label': 'Cancelado' },
            ],
            tabs: [
                { id: 'data', title: 'Pedido' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onOrderBookTableChange(0)
        optionsRequest(this, ['customerCoderpFantasy', 'localSale', 'userIdName'])
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
            activeTab: 'data',
        }, () => createEditTab('Detalhes do Pedido', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchOrderBookInfo())
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ width: '100%', flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={4}><MainTextField {...this.props} id='fantasialocal' value={this.state.orderBook.fantasialocal || ''} label='Local de venda' disabled='true' fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} id='nomevendedor' value={this.state.orderBook.nomevendedor || ''} label='Vendedor' disabled='true' fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} id='fantasiacliente' value={this.state.orderBook.fantasiacliente || ''} label='Cliente' disabled='true' fullWidth /></Grid>

                        <Grid item md={4}><MainTextField {...this.props} id='fantasiarepresentada' value={this.state.orderBook.fantasiarepresentada || ''} label='Representada' disabled='true' fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} id='nomeresponsavel' value={this.state.orderBook.nomeresponsavel || ''} label='Responsável' disabled='true' fullWidth /></Grid>
                        <Grid item md={4}><MainTextField {...this.props} id='situacaopedido' value={this.state.orderBook.situacaopedido || ''} label='Situação' disabled='true' fullWidth /></Grid>

                        <Grid item md={2}><MainTextField {...this.props} type='number' id='nrpedido' value={this.state.orderBook.nrpedido || ''} label='Nr. Pedido' disabled='true' fullWidth /></Grid>
                        <Grid item md={2}><MainTextField {...this.props} type='number' id='vlpedido' value={this.state.orderBook.vlpedido || ''} label='Vl. Pedido' disabled='true' fullWidth /></Grid>
                        <Grid item md={3}><MainDateTimeInput {...this.props} onlyDate id='dtpedido' value={this.state.orderBook.dtpedido || ''} label='Data Emissão' disabled='true' type='date' fullWidth /></Grid>

                        <Grid item md={3}>
                            <MainTabButton sx={{ width: '97%', '& button': { cursor: 'not-allowed' } }} {...this.props} onButtonClick={() => { }} title="Produto" />
                        </Grid>

                        <Accordion
                            {...this.props}
                            title='Nota Fiscal'
                            customCss={{ margin: '20px 10px 20px 7px' }}
                            content={
                                <>
                                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' } }}>
                                        <Grid item md={3}><MainTextField {...this.props} id='nrseriedanfe' value={this.state.orderBook.nrseriedanfe || ''} label='Série' disabled='true' fullWidth /></Grid>
                                        <Grid item md={3}><MainTextField {...this.props} type='number' id='nrdanfe' value={this.state.orderBook.nrdanfe || ''} label='Nr. Nota' disabled='true' fullWidth /></Grid>
                                        <Grid item md={3}><MainTextField {...this.props} type='number' id='vldanfe' value={this.state.orderBook.vldanfe || ''} label='Vl. Nota' disabled='true' fullWidth /></Grid>
                                        <Grid item md={3}><MainDateTimeInput {...this.props} id='dtemissao' value={this.state.orderBook.dtemissao || ''} label='Dt. Emissão' disabled='true' type='date' fullWidth /></Grid>
                                        <Grid item md={3}><MainSelectInput {...this.props} id='situacaodanfe' value={this.state.orderBook.situacaodanfe || ''} label='Situação' optionsList={this.state.danfeStatusOptions} disabled='true' fullWidth /></Grid>

                                        <Grid item md={3}>
                                            <MainTabButton sx={{ width: '97%', '& button': { cursor: 'not-allowed' } }} {...this.props} onButtonClick={() => { }} title="Produto" />
                                        </Grid>
                                    </Grid>
                                </>
                            }
                        />

                        <Accordion
                            {...this.props}
                            title='Títulos Emitidos'
                            customCss={{ margin: '20px 10px 20px 7px' }}
                            content={
                                <>
                                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' } }}>
                                        <Grid item md={3}><MainTextField {...this.props} id='nrserietitulo' value={this.state.orderBook.nrserietitulo || ''} label='Série' disabled='true' fullWidth /></Grid>
                                        <Grid item md={3}><MainTextField {...this.props} type='number' id='nrtitulo' value={this.state.orderBook.nrtitulo || ''} label='Nr. Título' disabled='true' fullWidth /></Grid>
                                        <Grid item md={3}><MainTextField {...this.props} type='number' id='qtparcela' value={this.state.orderBook.qtparcela || ''} label='Qt. Parcela' disabled='true' fullWidth /></Grid>

                                        <Grid item md={3}>
                                            <MainTabButton sx={{ width: '97%', '& button': { cursor: 'not-allowed' } }} {...this.props} onButtonClick={() => { }} title="Produto" />
                                        </Grid>
                                    </Grid>
                                </>
                            }
                        />

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

    handleChangeTextSituation = (event) => {
        handleChangeText(this.state.situation, event.target.id, event.target.value, () => this.setState({ menuId: '12' }))
    }

    onCloseEditTab = () => {
        this.setState({
            orderBook: {},
            isLoadingTab: true,
        })
    }

    onOrderBookTableChange = (page) => {
        this.setState({
            isLoadingOrderBookTable: true,
        })
        let config = {
            method: 'get',
            endpoint: 'order/book/search'
        }
        let form = {
            page: page,
            localSale: this.state.localSale,
            client: this.state.client,
            seller: this.state.seller,
            orderNumber: this.state.orderNumber,

            situation: JSON.stringify(this.state.situation),

            initialDate: this.state.initialDate,
            finalDate: this.state.finalDate,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    orderBookList: r.data.order_book,
                    orderBookColumns: r.data.columns,
                    orderBookTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingOrderBookTable: false,
                })
            }
        })
    }

    searchOrderBookInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'order/book/single'
        }
        let form = {
            id: this.state.selectedRow.idcarteirapedido
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    orderBook: r.data.order_book,
                    isLoadingTab: false,
                }, () => this.handleChangeTab())
            }
        })
    }


    render() {
        if (this.state.isLoading || this.state.isLoadingOptions) {
            return (
                <></>
            )
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Regras de Preço' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', md: 'column', lg: 'row' } }}>
                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" /></Grid>

                            <Grid item md={6}><MainSelectInput {...this.props} id='localSale' value={this.state.localSale} optionsList={this.state.localSaleOptions} label='Local de Venda' handleChange={this.handleChangeText} width='100%' /></Grid>
                            <Grid item md={6}><MainSelectInput {...this.props} id='seller' value={this.state.seller} optionsList={this.state.userIdNameOptions} label='Vendedor' handleChange={this.handleChangeText} width='100%' /></Grid>
                            <Grid item md={6}><MainSelectInput {...this.props} id='client' value={this.state.client} optionsList={this.state.customerCoderpFantasyOptions} label='Cliente' handleChange={this.handleChangeText} width='100%' /></Grid>

                            <Grid item md={6}>
                                <Box
                                    sx={{
                                        display: 'flex',
                                        flexDirection: { xs: 'column', md: 'column', lg: 'row'},
                                        justifyContent: 'center',
                                        alignItems: 'center',
                                        width: '100%',
                                        border: '2px solid',
                                        borderRadius: '5px',
                                        paddingTop: '25px',
                                        position: 'relative',
                                        borderColor: this.props.colors.grey[1100]
                                    }}

                                >
                                    <span style={{ position: 'absolute', fontSize: '15px', top: '0' }}>Situação:</span>
                                    <MainCheckBoxInput {...this.props} id='inPreparation' value={this.state.situation.inPreparation} label='Em Elaboração' handleChange={this.handleChangeTextSituation} />
                                    <MainCheckBoxInput {...this.props} id='salesOrder' value={this.state.situation.salesOrder} label='Pedido Venda' handleChange={this.handleChangeTextSituation} />
                                    <MainCheckBoxInput {...this.props} id='invoiced' value={this.state.situation.invoiced} label='Faturado' handleChange={this.handleChangeTextSituation} />
                                    <MainCheckBoxInput {...this.props} id='canceled' value={this.state.situation.canceled} label='Cancelado' handleChange={this.handleChangeTextSituation} />
                                </Box>
                            </Grid>
                            <Grid item md={2}><MainDateTimeInput {...this.props} onlyDate id='initialDate' value={this.state.initialDate} handleChange={this.handleChangeText} type='date' width='100%' /></Grid>
                            <Grid item md={2}><MainDateTimeInput {...this.props} onlyDate id='finalDate' value={this.state.finalDate} handleChange={this.handleChangeText} type='date' width='100%' /></Grid>
                            <Grid item md={2}><MainTextField sx={{ height: '100%', '& .MuiInputBase-root': { height: '100%' }, '& .MuiOutlinedInput-root': { height: '100%' } }} {...this.props} type='number' id='orderNumber' value={this.state.orderNumber} label='Nr. Pedido' handleChange={this.handleChangeText} width='100%' /></Grid>

                            <Grid item md={6}><Button sx={{ background: this.props.colors.custom['searchButtons'], width: '100%', height: '100%' }} {...this.props} variant='contained' onClick={() => this.onOrderBookTableChange(0)}>Buscar</Button></Grid>
                        </Grid>

                        {this.state.isLoadingOrderBookTable ?
                            <>
                                <Box paddingTop='10%'>
                                    <LoadingGif />
                                </Box>
                            </>
                            :
                            <>
                                <EditableTable
                                    {...this.props}
                                    id='orderbookTable'
                                    allowEdit
                                    noDeleteButton
                                    data={this.state.orderBookList}
                                    columns={this.state.orderBookColumns}
                                    rowId='idcarteirapedido'
                                    totalSize={this.state.orderBookTotalSize}
                                    onPageChange={this.onOrderBookTableChange}
                                    onEditRow={() => { }}
                                    onRowDoubleClick={(params) => this.createEditTab(params, false)}
                                    isLoading={this.state.isLoadingOrderBookTable}
                                    extraColumnsConfig={
                                        {
                                            'nrpedido': {
                                                'type': 'number'
                                            },
                                            'dtpedido': {
                                                'type': 'date'
                                            },
                                            'vlpedido': {
                                                'type': 'number'
                                            },
                                        }
                                    }
                                />
                            </>
                        }
                    </Box>
                </Box>
            </>
        )
    }
}

export default OrderBook;