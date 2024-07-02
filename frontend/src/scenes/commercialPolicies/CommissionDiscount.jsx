import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainLabel from "../../components/inputs/MainLabel";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class CommissionDiscount extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingCommissionDiscountTable: true,
            isLoadingCommissionDiscountRangeTable: true,

            menuId: '19',

            code: '',
            search: '',

            isANewCommissionDiscount: false,

            commissionDiscount: {},
            commissionDiscountList: [],
            commissionDiscountColumns: {},
            commissionDiscountTotalSize: '',

            commissionDiscountRange: {
                perdesconto: null,
                fatorcom: null,
            },
            commissionDiscountRangeList: [],
            commissionDiscountRangeColumns: {},
            commissionDiscountRangeTotalSize: '',

            tabs: [
                { id: 'data', title: 'Dados de Comissões por Faixa de Desconto' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onCommissionDiscountTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onCommissionDiscountTableChange(0)
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
            }, () => createEditTab('Comissão X Desconto', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewCommissionDiscount: false,
                selectedRow: params,
                activeTab: 'data',
            }, () => createEditTab('Comissão X Desconto', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteCommissionDiscountRange = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'discount/commission/single'
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
                }, () => this.searchCommissionDiscountInfo(0))
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
        if (this.state.isLoadingTab && !this.state.isANewCommissionDiscount) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchCommissionDiscountInfo(0))
            return
        }
        if (!this.state.commissionDiscount && !this.state.isANewCommissionDiscount) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={12}>
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
                                    <Grid item md={2}><MainTextField {...this.props} type='number' id='idcomdesconto' value={this.state.commissionDiscount.idcomdesconto} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                    <Grid item md={8}><MainTextField required {...this.props} id='descomissaodesc' value={this.state.commissionDiscount.descomissaodesc} label='Descrição da Variação' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '99%' }} /></Grid>
                                    <Grid item md={2}>
                                        <MainTabButton width='94%' {...this.props} onButtonClick={this.saveOrUpdateCommissionDiscount} title="Salvar" />
                                    </Grid>
                                </Grid>
                            </Box>
                        </Grid>

                        {!this.state.isANewCommissionDiscount ?
                            <>
                                <Grid item md={5}>
                                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                        <Grid item md={7}><MainTextField required {...this.props} type='percent' id='perdesconto' value={this.state.commissionDiscountRange.perdesconto || ''} label='Faixa de Desconto Até...  (%)' handleChange={this.handleChangeTextTabRange} fullWidth /></Grid>
                                        <Grid item md={5}><MainTextField required {...this.props} type='number' id='fatorcom' value={this.state.commissionDiscountRange.fatorcom || ''} label='Fator' handleChange={this.handleChangeTextTabRange} fullWidth /></Grid>
                                        <Grid item md={7}></Grid>
                                        <Grid item md={5}>
                                            <MainTabButton width='97%' {...this.props} onButtonClick={this.includeCommissionDiscountRange} title="Inserir" />
                                        </Grid>
                                    </Grid>
                                </Grid>

                                <Grid item md={7}>
                                    <EditableTable
                                        {...this.props}
                                        allowEdit
                                        noEditButton
                                        customMargin='0 10px 0 0 '
                                        height='40vh'
                                        id='idcomfaixa'
                                        data={this.state.commissionDiscountRangeList}
                                        columns={this.state.commissionDiscountRangeColumns}
                                        rowId='idcomfaixa'
                                        totalSize={this.state.commissionDiscountRangeTotalSize}
                                        onPageChange={this.searchCommissionDiscountInfo}
                                        onEditRow={this.onCommissionDiscountRangeTableEdit}
                                        onRowDoubleClick={() => { }}
                                        isLoading={this.state.isLoadingCommissionDiscountRangeTable}
                                        extraColumnsConfig={
                                            {
                                                'perdesconto': {
                                                    'type': 'percent',
                                                },
                                                'fatorcom': {
                                                    'type': 'number',
                                                },
                                            }
                                        }
                                    />
                                </Grid>
                            </>
                            :
                            <>
                            </>
                        }

                    </Grid>
                </Box>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.commissionDiscount, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabRange = (event) => {
        handleChangeText(this.state.commissionDiscountRange, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includeCommissionDiscountRange = () => {
        if (!this.state.commissionDiscountRange.perdesconto || !this.state.commissionDiscountRange.fatorcom) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'discount/commission/single'
        }
        let form = {
            id: this.state.selectedRow.idcomdesconto,
            commissionDiscountRange: this.state.commissionDiscountRange,
            type: 'addRange'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    commissionDiscountRange: {},
                }, () => this.searchCommissionDiscountInfo(0))
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
            commissionDiscount: {},
            commissionDiscountRange: {},
            commissionDiscountRangeList: [],
            commissionDiscountRangeColumns: {},
            commissionDiscountRangeTotalSize: '',
            isLoadingCommissionDiscountRangeTable: true,
            isANewCommissionDiscount: false
        })
    }

    onCommissionDiscountRangeTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                commissionDiscountRangeList: row
            }, () => this.deleteCommissionDiscountRange(extraParam))
        }
    }

    onCommissionDiscountTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/commission/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            code: this.state.code,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    commissionDiscountList: r.data.commission_discount,
                    commissionDiscountColumns: r.data.columns,
                    commissionDiscountTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingCommissionDiscountTable: false,
                })
            }
        })
    }

    saveOrUpdateCommissionDiscount = () => {
        if (!this.state.commissionDiscount.descomissaodesc) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'discount/commission/single'
        }
        let form = {
            id: this.state.commissionDiscount.idcomdesconto,
            commissionDiscount: this.state.commissionDiscount,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewCommissionDiscount) {
                    newState['isANewCommissionDiscount'] = false
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

    searchCommissionDiscountInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/commission/single'
        }
        let form = {
            id: this.state.selectedRow.idcomdesconto,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    commissionDiscount: r.data.commission_discount,

                    commissionDiscountRangeList: r.data.commission_discount_range,
                    commissionDiscountRangeColumns: r.data.columns,
                    commissionDiscountRangeTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingCommissionDiscountRangeTable: false,
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
                    <Header {...this.props} title='Comissões X Desconto' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '60px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '10% 60% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} type='number' id='code' value={this.state.code} label='Código' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onCommissionDiscountTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ code: '', search: '' })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewCommissionDiscount: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idcomdesconto'
                            allowEdit
                            noDeleteButton
                            data={this.state.commissionDiscountList}
                            columns={this.state.commissionDiscountColumns}
                            rowId='idcomdesconto'
                            totalSize={this.state.commissionDiscountTotalSize}
                            onPageChange={this.onCommissionDiscountTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingCommissionDiscountTable}
                            extraColumnsConfig={
                                {
                                    'idcomdesconto': {
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

export default CommissionDiscount;