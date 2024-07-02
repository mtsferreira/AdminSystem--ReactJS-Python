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
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class ComercialDiscount extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            isLoading: true,
            isLoadingConditionTable: true,
            isLoadingCascadeTable: true,
            isLoadingTab: true,
            menuId: '28',

            term: '',
            status: 'A',

            discountAcronym: '',
            discoutMax: '',
            discountIsCascade: 'N',

            discount: {},

            conditionList: [],
            conditionColumns: {},
            conditionTotalSize: '',

            termList: [],
            termColumns: {},
            termTotalSize: '',

            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'B', 'label': 'Bloqueado' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],

            discountOptions: [
                { 'value': 'S', 'label': 'Sim' },
                { 'value': 'N', 'label': 'Não' },
            ],

            activeTab: 'data',
            tabs: [
                { id: 'data', title: 'Dados' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onConditionTableChange(0)
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
        }, () => createEditTab('Eventos de Desconto Comercial', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deleteCascade = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'discount/cascade/term'
        }
        let form = {
            id: id,
        }
        defaultRequest(config, form).then((r) => {
            this.setState({
                alertMessage: r.data.message,
                alertType: r.status ? 'success' : 'error',
                showAlert: true,
            }, r.status ? () => this.onCascadeTableChange(0) : () => { })
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchCascade())
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            if (this.state.isLoadingCascadeTable) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.onCascadeTableChange(0))
                return
            }
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0 0 0' }}>
                        <Grid item md={2}><MainTextField disabled {...this.props} id='idcascata' value={this.state.discount.idcascata || ''} label='Código' handleChange={this.handleChangeTextTab} width='97%' /></Grid>
                        <Grid item md={7}><MainTextField required {...this.props} id='descascata' value={this.state.discount.descascata || ''} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>

                        <Grid item md={3}>
                            <MainTabButton width='97%' {...this.props} onButtonClick={this.saveCondition} title="Salvar" />
                        </Grid>

                        <Grid item md={12}><MainLabel {...this.props} variant="tabSubTitle" label="" /></Grid>
                        <Grid item md={4}>
                            <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' } }}>
                                <Grid item md={6}><MainTextField required {...this.props} id='discountAcronym' value={this.state.discountAcronym || ''} label='Sigla' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>
                                <Grid item md={6}><MainSelectInput required {...this.props} id='discountIsCascade' value={this.state.discountIsCascade || ''} optionsList={this.state.discountOptions} label='Desconto Cascata' handleChange={this.handleChangeTextNewTerm} fullWidth /></Grid>
                                <Grid item md={12}><MainTextField required {...this.props} type='percent' id='discoutMax' value={this.state.discoutMax || ''} label='Máximo (%)' handleChange={this.handleChangeTextNewTerm} width={{ xs: '97%', sm: '97%', md: '98%' }} /></Grid>

                                <Grid item md={6}>
                                    <MainTabButton width='97%' {...this.props} onButtonClick={this.saveCascade} title="Inserir" />
                                </Grid>
                            </Grid>
                        </Grid>
                        <Grid item md={8}>
                            <EditableTable
                                {...this.props}
                                allowEdit
                                noEditButton
                                customMargin='0'
                                height='50vh'
                                id='idcascatafaixa'
                                data={this.state.cascadeList}
                                columns={this.state.cascadeColumns}
                                rowId={'idcascatafaixa'}
                                totalSize={this.state.cascadeTotalSize}
                                onPageChange={this.onCascadeTableChange}
                                onEditRow={this.onCascadeTableEdit}
                                onRowDoubleClick={() => { }}
                                isLoading={this.state.isLoadingCascadeTable}
                                extraColumnsConfig={
                                    {
                                        'idcascatafaixa': {
                                            'type': 'number',
                                        },
                                        'tipocascata': {
                                            'type': 'select',
                                            'options': this.state.discountOptions
                                        },
                                        'permaximo': {
                                            'type': 'percent',
                                        },

                                    }
                                }
                            />
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
        handleChangeText(this.state.discount, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextNewTerm = (event) => {
        this.setState({ [event.target.id]: event.target.value }, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingConditionTable: true,
            isLoadingTab: true,
            isLoadingCascadeTable: true,
            discount: {},
        }, () => this.onConditionTableChange(0))
    }

    onConditionTableChange = (page) => {
        this.setState({ isLoadingConditionTable: true })
        let config = {
            method: 'get',
            endpoint: 'discount/cascade/search'
        }
        let form = {
            page: page,
            term: this.state.term,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    conditionList: r.data.discount,
                    conditionColumns: r.data.columns,
                    conditionTotalSize: r.data.total_size,
                    isLoading: false,
                    isLoadingConditionTable: false
                })
            }
        })
    }

    onCascadeTableChange = (page) => {
        this.setState({ isLoadingCascadeTable: true })
        let config = {
            method: 'get',
            endpoint: 'discount/cascade/term'
        }
        let form = {
            page: page,
            id: this.state.selectedRow.idcascata
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    cascadeList: r.data.cascade,
                    cascadeColumns: r.data.columns,
                    cascadeTotalSize: r.data.total_size,
                    isLoadingCascadeTable: false
                }, () => this.handleChangeTab())
            }
        })
    }

    onCascadeTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                cascadeList: row
            }, () => this.deleteCascade(extraParam))
        }
    }

    saveCondition = () => {
        let config = {
            method: 'post',
            endpoint: 'discount/cascade/single'
        }
        let form = {
            id: this.state.selectedRow.idcascata,
            discount: this.state.discount
        }
        defaultRequest(config, form).then((r) => {
            this.setState({
                alertMessage: r.data.message,
                alertType: r.status ? 'success' : 'error',
                showAlert: true,
            })
        })
    }

    saveCascade = () => {
        let config = {
            method: 'post',
            endpoint: 'discount/cascade/term'
        }
        let form = {
            id: this.state.selectedRow.idcascata,
            discount: {
                idcascata: this.state.selectedRow.idcascata,
                sigla: this.state.discountAcronym,
                permaximo: this.state.discoutMax,
                tipocascata: this.state.discountIsCascade
            }
        }
        defaultRequest(config, form).then((r) => {
            this.setState({
                alertMessage: r.data.message,
                alertType: r.status ? 'success' : 'error',
                showAlert: true,
            }, r.status ? () => this.onCascadeTableChange(0) : () => { })
        })
    }

    searchCascade = () => {
        let config = {
            method: 'get',
            endpoint: 'discount/cascade/single'
        }
        let form = {
            id: this.state.selectedRow.idcascata
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState(({
                    discount: r.data.discount,
                    isLoadingTab: false
                }), () => this.handleChangeTab())
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
                    <Header {...this.props} title='Desconto Comercial' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '20px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '75% 25%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='term' value={this.state.term || ''} label='Pesquisa' handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onConditionTableChange(0)} z>Buscar</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            allowEdit
                            noDeleteButton
                            id='idcascata'
                            data={this.state.conditionList}
                            columns={this.state.conditionColumns}
                            rowId={'idcascata'}
                            totalSize={this.state.conditionTotalSize}
                            onPageChange={this.onConditionTableChange}
                            onRowDoubleClick={(params) => this.createEditTab(params)}
                            isLoading={this.state.isLoadingConditionTable}
                            extraColumnsConfig={
                                {
                                    'idcascata': {
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

export default ComercialDiscount;