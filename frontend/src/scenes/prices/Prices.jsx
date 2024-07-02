import React from "react";
import ReactDOM from "react-dom";

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

import { addLastAccess } from "../../utils/layout";
import { Box, Button, Grid, Typography } from "@mui/material";
import { changeActiveTabStyle, createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class Prices extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,
            menuId: '9',

            isLoading: true,
            isLoadingTab: true,
            isLoadingPriceTable: true,
            isLoadingTermTable: true,
            isLoadingProductTable: true,

            search: '',
            isCurrent: false,
            isExpired: false,

            price: {},
            priceList: [],
            priceColumns: {},
            priceTotalSize: '',

            productList: [],
            productColumns: {},
            productTotalSize: '',

            termList: [],
            termColumns: {},
            termTotalSize: '',

            priceRulesOptions: [],
            volumeOptions: [],
            packagingOptions: [
                { 'value': '0', 'label': 'Unidade' },
                { 'value': '1', 'label': 'Caixa 1' },
                { 'value': '2', 'label': 'Caixa 2' },
                { 'value': '3', 'label': 'Todas' }
            ],
            shippingOptions: [
                { 'value': 0, 'label': 'SIF' },
                { 'value': 1, 'label': 'FOB' },
                { 'value': 2, 'label': 'Sem Frete' }
            ],

            activeTab: 'basicInfos',
            tabs: [
                { id: 'basicInfos', title: 'Informações' },
                { id: 'products', title: 'Produtos' },
                // {id: 'localSale', title: 'Locais de Venda'}
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        optionsRequest(this, ['priceRules', 'volume'])
        this.onPricesTableChange(0)
    }

    createEditTab = (params) => {
        this.setState({ selectedRow: params, isLoadingTab: true }, () => createEditTab('Informações do Preço', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deleteTableRow = (endpoint, id) => {
        let config = {
            method: 'delete',
            endpoint: endpoint
        }
        let form = {
            id: id
        }

        defaultRequest(config, form).then((r) => {
            this.setState({
                alertType: r.status ? 'success' : 'error',
                alertMessage: r.data.message,
                showAlert: true,
            }, () => this.onPricesTableChange(0))
        })
    }

    deleteTableRowTab = (endpoint, id) => {
        let config = {
            method: 'delete',
            endpoint: endpoint
        }
        let form = {
            id: id
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    isLoadingTermTable: true
                }, () => this.handleChangeTab())
            }
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchPriceInfo())
            return
        }
        if (!this.state.price && !this.state.isANewLocalSale) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'basicInfos') {
            if (this.state.isLoadingTermTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onTermTableChange(0))
                return
            }
            context =
                <>
                    <Box sx={{ flexGrow: 1 }}>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={3}><MainTextField {...this.props} disabled id='codtabela' value={this.state.price.codtabela || ''} label='Código ERP' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={6}><MainTextField {...this.props} disabled id='destabela' value={this.state.price.destabela || ''} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '97%' }} /></Grid>
                            <Grid item md={3}><MainSelectInput {...this.props} disabled id='embtabela' value={this.state.price.embtabela || ''} optionsList={this.state.packagingOptions} label='Embalagem' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={4}><MainDateTimeInput {...this.props} type='date' disabled id='datainicial' value={this.state.price.datainicial || ''} label='Data Inicial' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={4}><MainDateTimeInput {...this.props} type='date' disabled id='datafinal' value={this.state.price.datafinal || ''} label='Data Final' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={4}><MainDateTimeInput {...this.props} type='date' disabled id='dtatualizacao' value={this.state.price.dtatualizacao || ''} label='Data Atualização' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '97%' }} /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} type='percent' id='permargdesejavel' value={this.state.price.permargdesejavel || ''} label='M. Desejável (%)' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} type='percent' id='permargminima' value={this.state.price.permargminima || ''} label='M. Mínima (%)' handleChange={this.handleChangeTextTab} /></Grid>
                            <Grid item md={4}><MainTextField required {...this.props} type='percent' id='perdesconto' value={this.state.price.perdesconto || ''} label='Desconto (%)' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                            <Grid item md={5}><MainSelectInput required {...this.props} id='idvolume' value={this.state.price.idvolume || ''} optionsList={this.state.volumeOptions} label='Desconto por Volume' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                            <Grid item md={2}><MainSelectInput {...this.props} id='tipofrete' value={this.state.price.tipofrete || ''} defaultValue={this.state.shippingOptions[2]} optionsList={this.state.shippingOptions} label='Tipo de Frete' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                            <Grid item md={3}><MainSelectInput required {...this.props} id='idprecoregra' value={this.state.price.idprecoregra || ''} optionsList={this.state.priceRulesOptions} label='Regra de Preço' handleChange={this.handleChangeTextTab} width='97%' /></Grid>

                            <Grid item md={2}>
                                <MainTabButton sx={{ width: { xs: '97%', md: '97%', lg: '94%' }} } {...this.props} onButtonClick={this.savePrice} title="Salvar" />
                            </Grid>

                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Prazos Médios" /></Grid>
                            <Grid item md={5}>
                                <Grid container columnSpacing={1} rowSpacing={2}>
                                    <Grid item md={6}><MainTextField required {...this.props} type='number' id='termDays' value={this.state.termDays || ''} label='Dias' width='98%' handleChange={this.handleChangeTextTerm} /></Grid>

                                    <Grid item md={6}>
                                        <MainTabButton width='94%' {...this.props} onButtonClick={this.saveTerm} title="Adicionar" />
                                    </Grid>

                                </Grid>
                            </Grid>

                            <Grid item md={7} sx={{ marginTop: '-30px' }}>
                                <EditableTable
                                    {...this.props}
                                    id='termTable'
                                    height='35vh'
                                    allowEdit
                                    noEditButton
                                    data={this.state.termList}
                                    columns={this.state.termColumns}
                                    rowId={'idprecoprazo'}
                                    totalSize={this.state.termTotalSize}
                                    onPageChange={this.onTermTableChange}
                                    onEditRow={this.onTermTableEdit}
                                    onRowDoubleClick={() => { }}
                                    isLoading={this.state.isLoadingTermTable}
                                    extraColumnsConfig={
                                        {
                                            'prazodias': {
                                                'type': 'number'
                                            },
                                        }
                                    }
                                />
                            </Grid>
                        </Grid>
                    </Box>
                </>
        } else if (page === 'products') {
            if (this.state.isLoadingProductTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onProductTableChange(0))
                return
            }
            context =
                <>
                    <EditableTable
                        {...this.props}
                        id='termTable'
                        customMargin='0px'
                        data={this.state.productList}
                        columns={this.state.productColumns}
                        rowId={'idproduto'}
                        totalSize={this.state.productTotalSize}
                        onPageChange={this.onProductTableChange}
                        onRowDoubleClick={() => { }}
                        isLoading={this.state.isLoadingTermTable}
                    />
                </>
        } else if (page === 'localSale') {
            context =
                <>

                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTerm = (event) => {
        this.setState({ [event.target.id]: event.target.value }, () => this.handleChangeTab())
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.price, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            price: {},
            isLoadingTab: true,
        })
    }

    onPricesTableChange = (page) => {
        this.setState({ isLoadingPriceTable: true })
        let config = {
            method: 'get',
            endpoint: 'price'
        }
        let form = {
            page: page,
            term: this.state.search,
            isCurrent: this.state.isCurrent,
            isExpired: this.state.isExpired
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    priceList: r.data.price,
                    priceColumns: r.data.columns,
                    priceTotalSize: r.data.total_size,
                    isLoadingPriceTable: false,
                    isLoading: false
                })
            }
        })
    }

    onPricesTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                priceList: row
            }, () => this.deleteTableRow('price/single', extraParam))
        }
    }

    onProductTableChange = (page) => {
        this.setState({ isLoadingProductTable: true })
        let config = {
            method: 'get',
            endpoint: 'price/product'
        }
        let form = {
            id: this.state.selectedRow.idpreco,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productList: r.data.product_price,
                    productColumns: r.data.columns,
                    productTotalSize: r.data.total_size,
                    isLoadingProductTable: false,
                    activeTab: 'products'
                }, () => this.handleChangeTab())
            }
        })
    }

    onTermTableChange = (page) => {
        this.setState({ isLoadingTermTable: true })
        let config = {
            method: 'get',
            endpoint: 'price/term'
        }
        let form = {
            id: this.state.selectedRow.idpreco,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    termList: r.data.term,
                    termColumns: r.data.columns,
                    termTotalSize: r.data.total_size,
                    isLoadingTermTable: false,
                }, () => this.handleChangeTab())
            }
        })
    }

    onTermTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                termList: row
            }, () => this.deleteTableRowTab('price/term', extraParam))
        }
    }

    savePrice = () => {
        let config = {
            method: 'post',
            endpoint: 'price/single'
        }
        let form = {
            id: this.state.selectedRow.idpreco,
            price: this.state.price
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    grouper: {}
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

    saveTerm = () => {
        if (!this.state.termDays
        ) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'price/term'
        }
        let form = {
            id: this.state.selectedRow.idpreco,
            days: this.state.termDays
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,

                    isLoadingTermTable: true,
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true,
                })
            }
        })
    }

    searchPriceInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'price/single'
        }
        let form = {
            id: this.state.selectedRow.idpreco
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var price = r.data.price
                price.tipofrete = price.tipofrete ?? 2
                this.setState({
                    price: r.data.price,
                    isLoadingTab: false
                }, () => this.handleChangeTab())
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
                    <Header {...this.props} title='Tabela de Preços' menuId={this.state.menuId} showFav />
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
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Pesquisar' handleChange={this.handleChangeText} width='100%' />
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
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onPricesTableChange(0)}>Buscar</Button>
                        </Box>
                        <EditableTable
                            {...this.props}
                            id='priceTable'
                            data={this.state.priceList}
                            columns={this.state.priceColumns}
                            rowId={'idpreco'}
                            totalSize={this.state.priceTotalSize}
                            onPageChange={this.onPricesTableChange}
                            onEditRow={this.onPricesTableEdit}
                            onRowDoubleClick={this.createEditTab}
                            isLoading={this.state.isLoadingPriceTable}
                            extraColumnsConfig={
                                {
                                    'codtabela': {
                                        'type': 'number'
                                    },
                                    'datainicial': {
                                        'type': 'date'
                                    },
                                    'datafinal': {
                                        'type': 'date'
                                    },
                                    'dtatualizacao': {
                                        'type': 'date'
                                    },
                                    'embtabela': {
                                        'type': 'select',
                                        'options': this.state.packagingOptions
                                    },
                                    'permargdesejavel': {
                                        'type': 'percent'
                                    },
                                    'permargminima': {
                                        'type': 'percent'
                                    },
                                    'perdesconto': {
                                        'type': 'percent'
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

export default Prices