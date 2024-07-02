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

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class Product extends React.Component {
    constructor(props) {
        super(props)
        this.alterMessagesRef = React.createRef()
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            isLoading: true,
            isLoadingTab: true,
            isLoadingProductTable: true,
            isLoadingProductLocalTable: true,
            isLoadingProductMessageTable: true,
            isLoadingProductStructureInfo: true,
            isLoadingProductDimensionsTable: true,
            isLoadingProductBrandsManufacturersTable: true,
            menuId: '7',
            search: '',

            product: {},
            productList: [],
            productColumns: {},
            productTotalSize: '',

            productBrandsManufaturersList: [],
            productBrandsManufaturersColumns: {},
            productBrandsManufaturersTotalSize: '',

            productDimensions: {},
            productDimensionsList: [],
            productDimensionsColumns: {},
            productDimensionsTotalSize: '',

            productLocal: {},
            productLocalList: [],
            productLocalColumns: {},
            productLocalTotalSize: '',

            isEditingMessage: false,
            productMessage: {},
            productMessageList: [],
            productMessageColumns: {},
            productMessageTotalSize: '',

            productStructure: {},

            categoryOptions: [],
            allowsNegativeBalanceOptions: [
                { 'value': 'S', 'label': 'Sim' },
                { 'value': 'N', 'label': 'Não' }
            ],
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'B', 'label': 'Bloqueado' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],

            activeTab: 'data',
            tabs: [
                { id: 'data', title: 'Produto' },
                { id: 'message', title: 'Mensagens' },
                { id: 'brandsmanufactures', title: 'Marcas e Fabricantes' },
                { id: 'productstructure', title: 'Estrutura de Produto' },
                { id: 'weightsanddimensions', title: 'Pesos e Dimensões' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onProductTableChange(0)
        optionsRequest(this, ['category'])
    }

    componentDidUpdate() {
        if (this.state.isEditingMessage) {
            if (this.alterMessagesRef.current) {
                this.alterMessagesRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
            activeTab: 'data',
        }, () => createEditTab('Cadastro de Produto', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    editTableRow = (endpoint, origin, infos) => {
        let config = {
            method: 'post',
            endpoint: endpoint
        }

        let form = {
            id: infos.idprodutolocal,
            [origin]: infos
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.handleChangeTab()
            }
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchProductInfo())
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={2}><MainTextField {...this.props} type='number' id='codsecundario' value={this.state.product.codsecundario || ''} label='Código Secundário' handleChange={this.handleChangeTextTab} disabled='true' fullWidth /></Grid>
                        <Grid item md={8}><MainTextField {...this.props} id='dessecundaria' value={this.state.product.dessecundaria || ''} label='Descrição Secundária' handleChange={this.handleChangeTextTab} disabled='true' fullWidth /></Grid>
                        <Grid item md={2}><MainSelectInput {...this.props} id='situacao' value={this.state.product.situacao || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} disabled='true' fullWidth /></Grid>

                        <Grid item md={6}><MainTextField {...this.props} id='informacao.desaplicacao' value={this.state.product.informacao.desaplicacao || ''} label='Aplicação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainTextField {...this.props} id='informacao.destecnica' value={this.state.product.informacao.destecnica || ''} label='Descrição Técnica' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>

                        <Grid item md={2}>
                            <MainTabButton sx={{width: { xs: '97%', sm: '97%', md: '96%'}}} {...this.props} onButtonClick={this.saveProduct} title="Salvar" />
                        </Grid>
                    </Grid>
                </Box>
        } else if (page === 'message') {
            if (this.state.isLoadingProductMessageTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onProductMessageTableChange(0))
                return
            }
            context =
                <>
                    <MainLabel {...this.props} variant="tabSubSubTitle" label="Duplo clique para editar" />
                    <Box>
                        <EditableTable
                            {...this.props}
                            id='productMessageTable'
                            allowEdit
                            noDeleteButton
                            height='55vh'
                            data={this.state.productMessageList}
                            columns={this.state.productMessageColumns}
                            rowId={'idlocal'}
                            totalSize={this.state.productMessageTotalSize}
                            onPageChange={this.onProductMessageTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.onMessagesRowDoubleClick(params)}
                            isLoading={this.state.isLoadingProductMessageTable}
                        />
                    </Box>

                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '5px 0' }}>
                        {this.state.isEditingMessage ?
                            <>
                                <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Alterar Mensagens" /></Grid>
                                <Grid item md={2}><MainTextField {...this.props} type='number' id='local.coderp' value={this.state.productMessage.local.coderp || ''} label='Código ERP' handleChange={this.handleChangeTextMessageTab} disabled='true' fullWidth /></Grid>
                                <Grid item md={3}><MainTextField {...this.props} type='number' id='local.cnpj' value={this.state.productMessage.local.cnpj || ''} label='CNPJ' handleChange={this.handleChangeTextMessageTab} disabled='true' fullWidth /></Grid>
                                <Grid item md={7}><MainTextField {...this.props} id='local.fantasia' value={this.state.productMessage.local.fantasia || ''} label='Fantasia' handleChange={this.handleChangeTextMessageTab} disabled='true' fullWidth /></Grid>

                                <Grid item md={4}><MainTextField {...this.props} id='mensagem1' value={this.state.productMessage.mensagem1 || ''} label='Mensagem 1' handleChange={this.handleChangeTextMessageTab} fullWidth /></Grid>
                                <Grid item md={4}><MainTextField {...this.props} id='mensagem2' value={this.state.productMessage.mensagem2 || ''} label='Mensagem 2' handleChange={this.handleChangeTextMessageTab} fullWidth /></Grid>
                                <Grid item md={4}><MainTextField {...this.props} id='mensagem3' value={this.state.productMessage.mensagem3 || ''} label='Mensagem 3' handleChange={this.handleChangeTextMessageTab} fullWidth /></Grid>

                                <Grid ref={this.alterMessagesRef} item md={2}>
                                    <MainTabButton sx={{width: { xs: '97%', sm: '97%', md: '96%'}}} {...this.props} onButtonClick={this.saveProductMessage} title="Salvar" />
                                </Grid>

                            </> :
                            <></>}
                    </Grid>
                </>
        } else if (page === 'brandsmanufactures') {
            if (this.state.isLoadingProductBrandsManufacturersTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onProductBrandsManufacturersChange(0))
                return
            }
            context =
                <>
                    <Box>
                        <EditableTable
                            height='55vh'
                            {...this.props}
                            id='productNrandsManufacturersTable'
                            data={this.state.productBrandsManufaturersList}
                            columns={this.state.productBrandsManufaturersColumns}
                            rowId={'idproduto'}
                            totalSize={this.state.productBrandsManufaturersTotalSize}
                            onPageChange={this.onProductBrandsManufacturersChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingProductBrandsManufacturersTable}
                        />
                    </Box>
                </>

        } else if (page === 'productstructure') {
            if (this.state.isLoadingProductStructureInfo) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchProductStructureInfo())
                return
            }
            context =
                <>
                    <Box>
                        <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                            <Grid item md={4}><MainSelectInput required {...this.props} id='categoria' value={this.state.productStructure.categoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextStructureTab} fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='familia.descricao' value={this.state.productStructure.familia.descricao || ''} label='Família' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='ggrupo.descricao' value={this.state.productStructure.ggrupo.descricao || ''} label='Grande Grupo' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='grupo.descricao' value={this.state.productStructure.grupo.descricao || ''} label='Grupo' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='sgrupo.descricao' value={this.state.productStructure.sgrupo.descricao || ''} label='Sub Grupo' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>

                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Configurações Fiscais" /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='ncm' value={this.state.productStructure.ncm || ''} type='number' label='NCM' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='origem.descricao' value={this.state.productStructure.origem.descricao || ''} label='Origem do Produto' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>
                            <Grid item md={4}><MainTextField {...this.props} id='tipoproduto.descricao' value={this.state.productStructure.tipoproduto.descricao || ''} label='Tipo de Produto' handleChange={this.handleChangeTextStructureTab} disabled='true' fullWidth /></Grid>

                            <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="Configurações" /></Grid>
                            <Grid item md={4}><MainTextField required {...this.props} type='percent' id='percomissao' value={this.state.productStructure.percomissao || ''} label='Comissão (%)' handleChange={this.handleChangeTextStructureTab} fullWidth /></Grid>
                            <Grid item md={4}><MainTextField required {...this.props} type='percent' id='perdescmaximo' value={this.state.productStructure.perdescmaximo || ''} label='Desconto Máximo (%)' handleChange={this.handleChangeTextStructureTab} fullWidth /></Grid>

                            <Grid item md={2}>
                                <MainTabButton sx={{width: { xs: '97%', sm: '97%', md: '96%'}}} {...this.props} onButtonClick={this.saveProductStructure} title="Salvar" />
                            </Grid>
                        </Grid>
                    </Box>
                </>

        } else if (page === 'weightsanddimensions') {
            if (this.state.isLoadingProductDimensionsTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onProductDimensionsTableChange(0))
                return
            }
            if (this.state.isLoadingProductLocalTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onProductLocalTableChange(0))
                return
            }
            context =
                <>
                    <Grid container columnSpacing={1} rowSpacing={2} margin='5px 0'></Grid>
                    <Grid item md={12}>
                        <EditableTable
                            height='30vh'
                            {...this.props}
                            id='productDimensionsTable'
                            data={this.state.productDimensionsList}
                            columns={this.state.productDimensionsColumns}
                            rowId={'id'}
                            totalSize={this.state.productDimensionsTotalSize}
                            onPageChange={this.onProductDimensionsTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingProductDimensionsTable}
                        />
                    </Grid>

                    <Grid item md={12} sx={{ margin: '20px 0 0 0' }}><MainLabel {...this.props} variant="tabSubTitle" label="Duplo clique para editar" /></Grid>

                    <Grid item md={12}>
                        <EditableTable
                            height='50vh'
                            {...this.props}
                            id='productLocalTable'
                            allowEdit
                            allowEditOnRow
                            noDeleteButton
                            noAddRow
                            data={this.state.productLocalList}
                            columns={this.state.productLocalColumns}
                            rowId={'id'}
                            totalSize={this.state.productLocalTotalSize}
                            onPageChange={this.onProductLocalTableChange}
                            onEditRow={this.onProductLocalTableEdit}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingProductLocalTable}
                            extraColumnsConfig={
                                {
                                    'local.cnpj': {
                                        'disabled': true
                                    },
                                    'local.coderp': {
                                        'disabled': true
                                    },
                                    'local.fantasia': {
                                        'disabled': true
                                    },
                                    'permitirsaldonegativo': {
                                        'type': 'select',
                                        'options': this.state.allowsNegativeBalanceOptions
                                    },
                                    'multvenda': {
                                        'type': 'number'
                                    },
                                    'estoquepadrao': {
                                        'type': 'number'
                                    },
                                    'estoqueminimo': {
                                        'type': 'number'
                                    },
                                    'minvenda': {
                                        'type': 'number'
                                    },
                                }
                            }
                        />
                    </Grid>

                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.product, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextMessageTab = (event) => {
        handleChangeText(this.state.productMessage, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextStructureTab = (event) => {
        handleChangeText(this.state.productStructure, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            Product: {},
            isLoadingTab: true,
            isEditingMessage: false,
            isLoadingProductLocalTable: true,
            isLoadingProductMessageTable: true,
            isLoadingProductStructureInfo: true,
            isLoadingProductDimensionsTable: true,
            isLoadingProductBrandsManufacturersTable: true,
        })
    }

    onMessagesRowDoubleClick = (params) => {
        this.setState({
            productMessage: params,
            isEditingMessage: true,
        }, () => this.handleChangeTab());
    }

    onProductBrandsManufacturersChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/brandsmanufacturers/single'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idproduto,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productBrandsManufaturersList: r.data.product_brands_manufacturers,
                    productBrandsManufaturersColumns: r.data.columns,
                    productBrandsManufaturersTotalSize: r.data.total_size,
                    isLoadingProductBrandsManufacturersTable: false,
                    isLoadingProductMessageTable: true,
                    isLoadingProductDimensionsTable: true,
                    activeTab: 'brandsmanufactures',
                }, () => this.handleChangeTab())
            }
        })
    }

    onProductDimensionsTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/dimensions/single'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idproduto,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                const updatedProductDimensionsList = r.data.product_dimensions.map((item, index) => {

                    const uniqueId = `${item.idproduto}_${index}`;
                    return { ...item, id: uniqueId };
                })
                this.setState({
                    productDimensionsList: updatedProductDimensionsList,
                    productDimensionsColumns: r.data.columns,
                    productDimensionsTotalSize: r.data.total_size,
                    isLoadingProductDimensionsTable: false,
                    isLoadingProductBrandsManufacturersTable: true,
                    isLoadingProductMessageTable: true,
                    activeTab: 'weightsanddimensions',
                }, () => this.handleChangeTab())
            }
        })
    }

    onProductLocalTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/local/single'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idproduto,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                const updatedProductLocalList = r.data.product_local.map((item, index) => {

                    const uniqueId = `${item.idproduto}_${index}`;
                    return { ...item, id: uniqueId };
                })
                this.setState({
                    productLocalList: updatedProductLocalList,
                    productLocalColumns: r.data.columns,
                    productLocalTotalSize: r.data.total_size,
                    isLoadingProductLocalTable: false,
                    activeTab: 'weightsanddimensions'
                }, () => this.handleChangeTab())
            }
        })
    }

    onProductLocalTableEdit = (row, method, extraParam) => {
        if (method === 'edit') {
            this.setState({
                productLocalList: row
            }, () => this.editTableRow('product/local/single', 'productLocal', extraParam))
        }
    }

    onProductMessageTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/message/single'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idproduto,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productMessageList: r.data.product_message, //product_messsage.local
                    productMessageColumns: r.data.columns,
                    productMessageTotalSize: r.data.total_size,
                    isLoadingProductMessageTable: false,
                    isLoadingProductBrandsManufacturersTable: true,
                    isLoadingProductDimensionsTable: true,
                    activeTab: 'message',
                }, () => this.handleChangeTab())
            }
        })
    }

    onProductTableChange = (page) => {
        this.setState({
            isLoadingProductTable: true
        })
        let config = {
            method: 'get',
            endpoint: 'product/search'
        }
        let form = {
            page: page,
            term: this.state.search,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productList: r.data.product,
                    productColumns: r.data.columns,
                    productTotalSize: r.data.total_size,
                    isLoadingProductTable: false,
                    isLoading: false,
                })
            }
        })
    }

    saveProduct = () => {
        let config = {
            method: 'post',
            endpoint: 'product/single'
        }
        let form = {
            id: this.state.selectedRow.idproduto,
            product: this.state.product
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
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

    saveProductMessage = () => {
        let config = {
            method: 'post',
            endpoint: 'product/message/single'
        }
        let form = {
            id: this.state.productMessage.idprodutomensagem,
            productMessage: this.state.productMessage
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                this.setState(prevState => ({
                    ...prevState, ...newState,
                    isEditingMessage: false
                }), () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    saveProductStructure = () => {
        let config = {
            method: 'post',
            endpoint: 'product/structure/single'
        }
        let form = {
            id: this.state.selectedRow.idproduto,
            productStructure: this.state.productStructure
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
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

    searchProductInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'product/single'
        }
        let form = {
            id: this.state.selectedRow.idproduto
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    product: r.data.product,
                    isLoadingTab: false,
                }, () => this.handleChangeTab())
            }
        })
    }

    searchProductStructureInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'product/structure/single'
        }
        let form = {
            id: this.state.selectedRow.idproduto
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productStructure: r.data.product_structure,
                    isLoadingProductStructureInfo: false,
                    activeTab: 'productstructure'
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
                    <Header {...this.props} title='Cadastro de Produto' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Produto" />
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
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Pesquisar' handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => { this.setState({ isLoadingProductTable: true }, () => this.onProductTableChange(0)) }}>Buscar</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='productTable'
                            allowEdit
                            noDeleteButton
                            data={this.state.productList}
                            columns={this.state.productColumns}
                            rowId={'idproduto'}
                            totalSize={this.state.productTotalSize}
                            onPageChange={this.onProductTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params)}
                            isLoading={this.state.isLoadingProductTable}
                            extraColumnsConfig={
                                {
                                    'sku': {
                                        'type': 'number',
                                    },
                                    'coderp': {
                                        'type': 'number',
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
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

export default Product;