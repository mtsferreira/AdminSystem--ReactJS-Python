import React from "react";
import ReactDOM from "react-dom";

import dayjs from "dayjs";
import EditableTable from "../../components/tables/EditableTable";
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


class Offers extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingOffersTable: true,
            isLoadingOffersStructureTable: true,
            isLoadingOffersLocalSaleTable: true,

            menuId: '17',

            search: '',
            isCurrent: false,
            isExpired: false,
            localsale: '',

            isANewOffers: false,

            offers: {},
            offersList: [],
            offersColumns: {},
            offersTotalSize: '',

            offersLocalSaleList: [],
            offersLocalSaleColumns: {},
            offersLocalSaleTotalSize: '',

            offersStructureList: [],
            offersStructureColumns: {},
            offersStructureTotalSize: '',
            offersStructure: {
                idproduto: null,
                idfamilia: null,
                idgrupo: null,
                idggrupo: null,
                idsgrupo: null,
                idmarca: null,
                idcategoria: null,
                idfabricante: null,
                idlinha: null,
                desoferta: null,
                desoferta2: null,
                qtoferta: null,
                qtminima: null,
                qtmaxima: null,
            },

            tabs: [
                { id: 'data', title: 'Cadastro de Oferta' },
                { id: 'localsale', title: 'Local de Venda' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onOffersTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onOffersTableChange(0)
        optionsRequest(this, ['bigGroup', 'brand', 'category', 'family', 'group', 'localSale', 'manufacturer', 'offer', 'product', 'productLine', 'subGroup'])
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                offers: {
                    dtinicial: dayjs().format('YYYY-MM-DD'),
                    dtfinal: dayjs().format('YYYY-MM-DD'),
                },
                tabs: [
                    { id: 'data', title: 'Cadastro de Oferta' },
                ],
            }, () => createEditTab('Ofertas', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewOffers: false,
                selectedRow: params,
                activeTab: 'data',
                tabs: [
                    { id: 'data', title: 'Cadastro de Oferta' },
                    { id: 'localsale', title: 'Local de Venda' },
                ],
            }, () => createEditTab('Ofertas', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteOffersLocalSale = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'offer/localsale/single'
        }
        let form = {
            id: this.state.selectedRow.idoferta,
            localsaleId: id
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.onOffersLocalSaleTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    deleteOffersStructure = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'offer/single'
        }
        let form = {
            id: id
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.searchOffersInfo(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab && !this.state.isANewOffers) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchOffersInfo(0))
            return
        }
        if (!this.state.offers && !this.state.isANewOffers) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={12} sx={{ width: '100%' }}>
                            <Box
                                width='99%'
                                border='1px solid'
                                borderRadius='5px'
                                padding='0 10px 10px 5px'
                                marginBottom='15px'
                                borderColor={this.props.colors.grey[1100]}
                                boxShadow={`3px 3px 3px ${this.props.colors.custom['boxShadow']}`}
                            >
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '10px 0' }}>
                                    <Grid item md={1}><MainTextField {...this.props} type='number' id='idoferta' value={this.state.offers.idoferta} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                    <Grid item md={5}><MainTextField required {...this.props} id='descricao' value={this.state.offers.descricao} label='Descrição da Oferta' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '100%' }} /></Grid>

                                    <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='dtinicial' value={this.state.offers.dtinicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                    <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='dtfinal' value={this.state.offers.dtfinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>

                                    <Grid item md={2}>
                                        <MainTabButton sx={{ width: { xs: '94%', sm: '94%', md: '95%' } }} {...this.props} onButtonClick={this.saveOrUpdateOffers} title="Salvar" />
                                    </Grid>
                                </Grid>
                            </Box>
                        </Grid>

                        {!this.state.isANewOffers ?
                            <>
                                <Grid item xs={12} sm={12} md={12}><MainSelectInput required {...this.props} id='idproduto' value={this.state.offersStructure.idproduto || ''} optionsList={this.state.productOptions} label='Produto' handleChange={this.handleChangeTextTabSelects} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idfamilia' value={this.state.offersStructure.idfamilia || ''} optionsList={this.state.familyOptions} label='Família' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idggrupo' value={this.state.offersStructure.idggrupo || ''} optionsList={this.state.bigGroupOptions} label='Grande Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idgrupo' value={this.state.offersStructure.idgrupo || ''} optionsList={this.state.groupOptions} label='Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idsgrupo' value={this.state.offersStructure.idsgrupo || ''} optionsList={this.state.subGroupOptions} label='Sub Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idmarca' value={this.state.offersStructure.idmarca || ''} optionsList={this.state.brandOptions} label='Marca' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idcategoria' value={this.state.offersStructure.idcategoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={8}><MainSelectInput {...this.props} id='idfabricante' value={this.state.offersStructure.idfabricante || ''} optionsList={this.state.manufacturerOptions} label='Fabricante' handleChange={this.handleChangeTextTabSelects} width={{ xs: '97%', sm: '97%', md: '98.5%' }} /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idlinha' value={this.state.offersStructure.idlinha || ''} optionsList={this.state.productLineOptions} label='Linha' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>

                                <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='percent' id='desoferta' value={this.state.offersStructure.desoferta || ''} label='Desconto (%)' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='percent' id='desoferta2' value={this.state.offersStructure.desoferta2 || ''} label='Desconto 2 (%)' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='number' id='qtoferta' value={this.state.offersStructure.qtoferta || ''} label='Qtd. Ofertada' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='number' id='qtminima' value={this.state.offersStructure.qtminima || ''} label='Qtd. Mínima' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='number' id='qtmaxima' value={this.state.offersStructure.qtmaxima || ''} label='Qtd. Máxima' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>

                                <Grid item xs={12} sm={12} md={2}>
                                    <MainTabButton sx={{ width: { xs: '97%', sm: '97%', md: '94%' } }} {...this.props} onButtonClick={this.includeOffersStructure} title="Inserir" />
                                </Grid>

                                <Grid item xs={12} sm={12} md={12} sx={{ width: '100%' }}>
                                    <Box width='99%'>
                                        <EditableTable
                                            {...this.props}
                                            id='idofertaestrutura'
                                            allowEdit
                                            noEditButton
                                            height='50vh'
                                            data={this.state.offersStructureList}
                                            columns={this.state.offersStructureColumns}
                                            rowId='idofertaestrutura'
                                            totalSize={this.state.offersStructureTotalSize}
                                            onPageChange={this.searchOffersInfo}
                                            onEditRow={this.onOffersStructureTableEdit}
                                            onRowDoubleClick={() => { }}
                                            isLoading={this.state.isLoadingOffersStructureTable}
                                            extraColumnsConfig={
                                                {
                                                    'idproduto_id': {
                                                        'type': 'select',
                                                        'options': this.state.productOptions
                                                    },
                                                    'idfamilia_id': {
                                                        'type': 'select',
                                                        'options': this.state.familyOptions
                                                    },
                                                    'idggrupo_id': {
                                                        'type': 'select',
                                                        'options': this.state.bigGroupOptions
                                                    },
                                                    'idgrupo_id': {
                                                        'type': 'select',
                                                        'options': this.state.groupOptions
                                                    },
                                                    'idsgrupo_id': {
                                                        'type': 'select',
                                                        'options': this.state.subGroupOptions
                                                    },
                                                    'idmarca_id': {
                                                        'type': 'select',
                                                        'options': this.state.brandOptions
                                                    },
                                                    'idcategoria_id': {
                                                        'type': 'select',
                                                        'options': this.state.categoryOptions
                                                    },
                                                    'idfabricante_id': {
                                                        'type': 'select',
                                                        'options': this.state.manufacturerOptions
                                                    },
                                                    'idlinha_id': {
                                                        'type': 'select',
                                                        'options': this.state.productLineOptions
                                                    },
                                                    'desoferta': {
                                                        'type': 'percent',
                                                    },
                                                    'desoferta2': {
                                                        'type': 'percent',
                                                    },
                                                }
                                            }
                                        />
                                    </Box>
                                </Grid>
                            </>
                            :
                            <>
                            </>
                        }
                    </Grid>
                </Box>
        } else if (page === 'localsale') {
            if (this.state.isLoadingOffersLocalSaleTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onOffersLocalSaleTableChange(0))
                return
            }
            context =
                <>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>

                        <Grid item md={10}><MainSelectInput required {...this.props} id='localsale' value={this.state.localsale} optionsList={this.state.localSaleOptions} label='Local de Venda' handleChange={this.handleChangeTextTabLocalSale} width='98%' /></Grid>

                        <Grid item md={2}>
                            <MainTabButton sx={{ width: { xs: '98%', sm: '98%', md: '95%' } }} {...this.props} onButtonClick={this.includeOffersLocalSale} title="Inserir" />
                        </Grid>

                        <Grid item md={12}>
                            <EditableTable
                                {...this.props}
                                height='40vh'
                                allowEdit
                                noEditButton
                                id='idlocal'
                                data={this.state.offersLocalSaleList}
                                columns={this.state.offersLocalSaleColumns}
                                rowId='idlocal_id'
                                totalSize={this.state.offersLocalSaleTotalSize}
                                onPageChange={this.onOffersLocalSaleTableChange}
                                onEditRow={this.onOffersLocalSaleTableEdit}
                                onRowDoubleClick={() => { }}
                                isLoading={this.state.isLoadingOffersLocalSaleTable}
                                extraColumnsConfig={
                                    {
                                        'idoferta_id': {
                                            'type': 'select',
                                            'options': this.state.offerOptions
                                        },
                                        'idlocal_id': {
                                            'type': 'select',
                                            'options': this.state.localSaleOptions
                                        },
                                    }
                                }
                            />
                        </Grid>
                    </Grid>
                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.offers, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabLocalSale = (event) => {
        this.setState({ [event.target.id]: event.target.value }, () => this.handleChangeTab())
    }

    handleChangeTextTabSelects = (event) => {
        handleChangeText(this.state.offersStructure, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includeOffersLocalSale = () => {
        if (!this.state.localsale) {
            this.setState({
                alertMessage: 'Necessário selecionar um local de venda.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'offer/localsale/single'
        }
        let form = {
            id: this.state.selectedRow.idoferta,
            localsale: this.state.localsale,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    offersStructure: {},
                }, () => this.onOffersLocalSaleTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    includeOffersStructure = () => {
        if (!this.state.offersStructure.idproduto) {
            this.setState({
                alertMessage: 'Necessário selecionar um produto.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'offer/single'
        }
        let form = {
            id: this.state.selectedRow.idoferta,
            offersStructure: this.state.offersStructure,
            type: 'addStructure'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    offersStructure: {},
                }, () => this.searchOffersInfo(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingTab: true,
            localsale: '',
            offers: {},
            offersStructure: {},
            offersStructureList: [],
            offersStructureColumns: {},
            offersStructureTotalSize: '',
            offersLocalSaleList: [],
            offersLocalSaleColumns: {},
            offersLocalSaleTotalSize: '',
            isLoadingOffersStructureTable: true,
            isLoadingOffersLocalSaleTable: true,
            isANewOffers: false
        })
    }

    onOffersLocalSaleTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'offer/localsale/single'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idoferta
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    offersLocalSaleList: r.data.offers_localsale,
                    offersLocalSaleColumns: r.data.columns,
                    offersLocalSaleTotalSize: r.data.total_size,

                    isLoadingOffersLocalSaleTable: false,
                    activeTab: 'localsale',
                }, () => this.handleChangeTab())
            }
        })

    }

    onOffersTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'offer/search'
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
                    offersList: r.data.offers,
                    offersColumns: r.data.columns,
                    offersTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingOffersTable: false,
                })
            }
        })
    }

    onOffersLocalSaleTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                offersLocalSaleList: row
            }, () => this.deleteOffersLocalSale(extraParam))
        }
    }

    onOffersStructureTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                offersStructureList: row
            }, () => this.deleteOffersStructure(extraParam))
        }
    }

    saveOrUpdateOffers = () => {
        if (!this.state.offers.descricao) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'offer/single'
        }
        let form = {
            id: this.state.offers.idoferta,
            offers: this.state.offers,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewOffers) {
                    newState['isANewOffers'] = false
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

    searchOffersInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'offer/single'
        }
        let form = {
            id: this.state.selectedRow.idoferta,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    offers: r.data.offers,

                    offersStructureList: r.data.offers_structure,
                    offersStructureColumns: r.data.columns,
                    offersStructureTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingOffersStructureTable: false,
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
                    <Header {...this.props} title='Ofertas' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '25px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '50% 17% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />

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

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onOffersTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewOffers: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idoferta'
                            allowEdit
                            noDeleteButton
                            data={this.state.offersList}
                            columns={this.state.offersColumns}
                            rowId='idoferta'
                            totalSize={this.state.offersTotalSize}
                            onPageChange={this.onOffersTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingOffersTable}
                            extraColumnsConfig={
                                {
                                    'idoferta': {
                                        'type': 'number'
                                    },
                                    'dtinicial': {
                                        'type': 'date'
                                    },
                                    'dtfinal': {
                                        'type': 'date'
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

export default Offers;