import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, getCityOptionsRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class salesRegion extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingsalesRegionTable: true,
            isLoadingsalesRegionSellerTable: true,
            isLoadingsalesRegionUfCityTable: true,
            isLoadingsalesRegionRepresentedTable: true,

            menuId: '33',

            search: '',
            status: 'A',
            regionid: '',
            isNewSaleRegion: false,

            selectUf: '',
            selectCity: '',
            cityOptionsByUf: [],

            newsalesRegionDescription: '',
            newsalesRegionStatus: '',

            salesRegion: {},
            salesRegionList: [],
            salesRegionUfCity: {},
            salesRegionColumns: {},
            salesRegionTotalSize: '',

            salesRegionSellerList: [],
            salesRegionSellerColumns: {},
            salesRegionSellerTotalSize: '',

            salesRegionUfCityList: [],
            salesRegionUfCityColumns: [],
            salesRegionUfCityTotalSize: '',

            salesRegionRepresentedList: [],
            salesRegionRepresentedColumns: {},
            salesRegionRepresentedTotalSize: '',

            activeTab: 'data',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Inativo' },
            ],
            tabs: [
                { id: 'data', title: 'UF / Cidade' },
                { id: 'seller', title: 'Vendedor' },
                { id: 'represented', title: 'Representada' },
                { id: 'representative', title: 'Representante' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onsalesRegionTableChange(0)
        optionsRequest(this, ['uf'])
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
        }, () => createEditTab('Regiões de Vendas', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deletesalesRegionUfCity = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'salesregion/single'
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
                }, () => this.searchsalesRegionUfCityInfo(0))
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
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchsalesRegionUfCityInfo(0))
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={2}><MainTextField {...this.props} type='number' id='idregiao' value={this.state.salesRegion.idregiao} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                        <Grid item md={6}><MainTextField required {...this.props} id='desregiao' value={this.state.salesRegion.desregiao} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '97%' }} /></Grid>
                        <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.salesRegion.situacao} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} /></Grid>


                        <Grid item md={2}>
                            <MainTabButton width='94%' {...this.props} onButtonClick={this.updatesalesRegion} title="Salvar" />
                        </Grid>
                    </Grid>

                    <MainLabel {...this.props} variant="tabSubTitle" label="UF / Cidade" />
                    <Grid 
                        container 
                        columnSpacing={1} 
                        rowSpacing={2}
                        sx={{
                            flexDirection: { xs: 'column', sm: 'column', md: 'row' },
                            margin: '15px 0',
                        }}
                    >
                        <Grid item md={2}><MainSelectInput {...this.props} id='uf' value={this.state.selectUf} optionsList={this.state.ufOptions} label='UF' handleChange={this.handleChangeTextSelectUfTab} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='cidade' value={this.state.selectCity} optionsList={this.state.cityOptionsByUf} label='Cidade' handleChange={this.handleChangeTextSelectCityTab} /></Grid>
                        
                        <Grid item md={2}>
                            <MainTabButton sx={{width: { xs: '94%', sm: '94%', md: '90%'}}} {...this.props} onButtonClick={this.savesalesRegionUfCity} title="Incluir" />
                        </Grid>
                    </Grid>

                    <EditableTable
                        {...this.props}
                        id='idregiao'
                        noEditButton
                        allowEdit
                        height='45vh'
                        data={this.state.salesRegionUfCityList}
                        columns={this.state.salesRegionUfCityColumns}
                        rowId='idregiaouf'
                        totalSize={this.state.salesRegionUfCityTotalSize}
                        onPageChange={this.searchsalesRegionUfCityInfo}
                        onEditRow={this.onsalesRegionUfCityTableEdit}
                        onRowDoubleClick={() => { }}
                        isLoading={this.state.isLoadingsalesRegionUfCityTable}
                    />
                </Box>
        } else if (page === 'seller') {
            if (this.state.isLoadingsalesRegionSellerTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onsalesRegionSellerTableChange(0))
                return
            }
            context =
                <>
                    <EditableTable
                        {...this.props}
                        id='idregiao'
                        noEditButton
                        data={this.state.salesRegionSellerList}
                        columns={this.state.salesRegionSellerColumns}
                        rowId='idusuario'
                        totalSize={this.state.salesRegionSellerTotalSize}
                        onPageChange={this.onsalesRegionSellerTableChange}
                        onEditRow={() => { }}
                        onRowDoubleClick={() => { }}
                        isLoading={this.state.isLoadingsalesRegionSellerTable}
                    />
                </>
        } else if (page === 'represented') {
            if (this.state.isLoadingsalesRegionRepresentedTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onsalesRegionRepresentedTableChange(0))
                return
            }
            context =
                <>
                    <EditableTable
                        {...this.props}
                        id='idregiao'
                        data={this.state.salesRegionRepresentedList}
                        columns={this.state.salesRegionRepresentedColumns}
                        rowId='idrepresentadaregiao'
                        totalSize={this.state.salesRegionRepresentedTotalSize}
                        onPageChange={this.onsalesRegionRepresentedTableChange}
                        onEditRow={() => { }}
                        onRowDoubleClick={() => { }}
                        isLoading={this.state.isLoadingsalesRegionRepresentedTable}
                    />
                </>
        } else if (page === 'representative') {
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextSelectCityTab = (event) => {
        this.setState({ selectCity: event.target.value }, () => this.handleChangeTab())
    }

    handleChangeTextSelectUfTab = (event) => {
        getCityOptionsRequest(this, event.target.value).then((r) => {
            this.setState({
                cityOptionsByUf: r.data.city_options,
                selectUf: event.target.value
            }, () => this.handleChangeTab())
        })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.salesRegion, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingTab: true,
            isLoadingsalesRegionUfCityTable: true,
            isLoadingsalesRegionSellerTable: true,
            salesRegion: {},
            selectCity: '',
            selectUf: '',
            activeTab: 'data'
        }, () => this.onsalesRegionTableChange(0))
    }

    onsalesRegionRepresentedTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'salesregion/represented'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idregiao,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    salesRegionRepresentedList: r.data.represented,
                    salesRegionRepresentedColumns: r.data.columns,
                    salesRegionRepresentedTotalSize: r.data.total_size,
                    isLoadingsalesRegionRepresentedTable: false,
                    activeTab: 'represented',

                    isLoadingsalesRegionSellerTable: true,
                }, () => this.handleChangeTab())
            }
        })
    }

    onsalesRegionSellerTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'salesregion/sellers'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idregiao,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    salesRegionSellerList: r.data.sellers,
                    salesRegionSellerColumns: r.data.columns,
                    salesRegionSellerTotalSize: r.data.total_size,
                    isLoadingsalesRegionSellerTable: false,
                    activeTab: 'seller',

                    isLoadingsalesRegionRepresentedTable: true,
                }, () => this.handleChangeTab())
            }
        })
    }

    onsalesRegionTableChange = (page) => {
        this.setState({ isLoadingsalesRegionTable: true })
        let config = {
            method: 'get',
            endpoint: 'salesregion/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            regionid: this.state.regionid
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    salesRegionList: r.data.sale_regions,
                    salesRegionColumns: r.data.columns,
                    salesRegionTotalSize: r.data.total_size,
                    isLoading: false,
                    isLoadingsalesRegionTable: false,
                })
            }
        })
    }

    onsalesRegionUfCityTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                salesRegionUfCityList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deletesalesRegionUfCity(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    updatesalesRegion = () => {
        let config = {
            method: 'post',
            endpoint: 'salesregion/single'
        }
        let form = {
            id: this.state.selectedRow.idregiao,
            salesRegion: this.state.salesRegion,
            type: 'updateDescription'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    selectCity: this.state.selectCity,
                    selectUf: this.state.selectUf
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

    savesalesRegion = () => {
        if (!this.state.newsalesRegionDescription || !this.state.newsalesRegionStatus) {
            this.setState({
                alertMessage: 'UF/Cidade inválido',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'salesregion/search'
        }
        let form = {
            infos: {
                desregiao: this.state.newsalesRegionDescription,
                situacao: this.state.newsalesRegionStatus
            }
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    newsalesRegionDescription: '',
                    newsalesRegionStatus: '',
                    menuId: 33
                }, () => this.onsalesRegionTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    savesalesRegionUfCity = () => {
        if (!this.state.selectUf || !this.state.selectCity) {
            this.setState({
                alertMessage: 'UF/Cidade inválido',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'salesregion/single'
        }
        let form = {
            id: this.state.selectedRow.idregiao,
            infos: {
                cidade: this.state.selectCity,
                uf: this.state.selectUf,
            },
            type: 'addUfCity'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    selectUf: this.state.selectUf,
                    selectCity: this.state.selectCity,
                }, () => this.searchsalesRegionUfCityInfo(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })


    }

    searchsalesRegionUfCityInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'salesregion/single'
        }
        let form = {
            id: this.state.selectedRow.idregiao,
            page: page,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                const updatedsalesRegionUfCityList = r.data.sale_regions_uf_city.map((item, index) => {

                    const uniqueId = `${item.idregiao}_${index}`;
                    return { ...item, id: uniqueId };
                })
                this.setState({
                    salesRegion: r.data.sale_regions,
                    salesRegionUfCityList: updatedsalesRegionUfCityList,
                    salesRegionUfCityColumns: r.data.columns,
                    salesRegionUfCityTotalSize: r.data.total_size,
                    isLoadingTab: false,
                    isLoadingsalesRegionUfCityTable: false
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
                    <Header {...this.props} title='Regiões de Venda' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr:'45px',
                                display:'grid',
                                gap:'15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '15% 55% 15% 15%',
                                },
                            }}
                           
                        >
                            <MainTextField {...this.props} type='number' id='regionid' value={this.state.regionid} label='Código' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onsalesRegionTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.setState({ isNewSaleRegion: true })}>Novo</Button>
                        </Box>

                        {this.state.isNewSaleRegion ?
                            <>
                                <Box className='outline-box'>
                                    <MainLabel sx={{ marginTop: '30px' }} {...this.props} variant="tabTitle" label="Cadastrar nova região de venda" />

                                    <Box
                                        mr='10px'
                                        display='grid'
                                        gap='8px'
                                        gridTemplateColumns='50% 19% 15.5% 15.5%'
                                    >
                                        <MainTextField {...this.props} id='newsalesRegionDescription' value={this.state.newsalesRegionDescription} label='Descrição' handleChange={this.handleChangeText} fullWidth />
                                        <MainSelectInput {...this.props} id='newsalesRegionStatus' value={this.state.newsalesRegionStatus} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} />

                                        <MainTabButton width='95%' {...this.props} onButtonClick={this.savesalesRegion} title="Salvar" />

                                        <MainTabButton width='95%' {...this.props} onButtonClick={() => this.setState({ isNewSaleRegion: false, newsalesRegionDescription: '', newsalesRegionStatus: '' })} title="Cancelar" />

                                    </Box>
                                </Box>
                            </>
                            : <></>}

                        <EditableTable
                            {...this.props}
                            id='idregiao'
                            allowEdit
                            noDeleteButton
                            data={this.state.salesRegionList}
                            columns={this.state.salesRegionColumns}
                            rowId='idregiao'
                            totalSize={this.state.salesRegionTotalSize}
                            onPageChange={this.onsalesRegionTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingsalesRegionTable}
                            extraColumnsConfig={
                                {
                                    'idregiao': {
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

export default salesRegion;