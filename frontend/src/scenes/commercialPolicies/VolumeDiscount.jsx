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
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class VolumeDiscount extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingVolumeDiscountTable: true,
            isLoadingVolumeRangeDiscounteTable: true,

            menuId: '22',

            code: '',
            search: '',
            isCurrent: false,
            isExpired: false,
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Cancelado' },
                { 'value': 'B', 'label': 'Bloqueado' },
            ],

            isANewVolumeDiscount: false,

            volumeDiscount: {},
            volumeDiscountList: [],
            volumeDiscountColumns: {},
            volumeDiscountTotalSize: '',

            volumeRangeDiscount: {
                vlcomprasde: null,
                vlcomprasate: null,
                perdesconto: null,
            },
            volumeRangeDiscountList: [],
            volumeRangeDiscountColumns: {},
            volumeRangeDiscountTotalSize: '',

            tabs: [
                { id: 'data', title: 'Desconto Volume' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onVolumeDiscountTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onVolumeDiscountTableChange(0)
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                volumeDiscount: {
                    datainicial: dayjs().format('YYYY-MM-DD'),
                    datafinal: dayjs().format('YYYY-MM-DD'),
                },
            }, () => createEditTab('Dados Desconto Volume', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewVolumeDiscount: false,
                selectedRow: params,
                activeTab: 'data',
            }, () => createEditTab('Dados Desconto Volume', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteVolumeRangeDiscount = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'discount/volume/single'
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
                }, () => this.searchVolumeDiscountInfo(0))
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
        if (this.state.isLoadingTab && !this.state.isANewVolumeDiscount) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchVolumeDiscountInfo(0))
            return
        }
        if (!this.state.volumeDiscount && !this.state.isANewVolumeDiscount) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <>
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
                                        <Grid item md={2}><MainTextField {...this.props} type='number' id='idvolume' value={this.state.volumeDiscount.idvolume} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                        <Grid item md={10}><MainTextField required {...this.props} id='desvolume' value={this.state.volumeDiscount.desvolume} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '99%' }} /></Grid>

                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datainicial' value={this.state.volumeDiscount.datainicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datafinal' value={this.state.volumeDiscount.datafinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                        <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.volumeDiscount.situacao} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} /></Grid>

                                        <Grid item md={4}></Grid>

                                        <Grid item md={2}>
                                            <MainTabButton width='94%' {...this.props} onButtonClick={this.saveOrUpdateVolumeDiscount} title="Salvar" />
                                        </Grid>
                                    </Grid>
                                </Box>
                            </Grid>

                            {!this.state.isANewVolumeDiscount ?
                                <>
                                    <Grid item md={2}><MainTextField required {...this.props} type='currency' id='vlcomprasde' value={this.state.volumeRangeDiscount.vlcomprasde || ''} label='Compras de...' handleChange={this.handleChangeTextTabRange} /></Grid>
                                    <Grid item md={2}><MainTextField required {...this.props} type='currency' id='vlcomprasate' value={this.state.volumeRangeDiscount.vlcomprasate || ''} label='Até...' handleChange={this.handleChangeTextTabRange} /></Grid>
                                    <Grid item md={2}><MainTextField required {...this.props} type='percent' id='perdesconto' value={this.state.volumeRangeDiscount.perdesconto || ''} label='Desconto (%)' handleChange={this.handleChangeTextTabRange} /></Grid>

                                    <Grid item md={4}></Grid>

                                    <Grid item md={2}>
                                        <MainTabButton width='94%' {...this.props} onButtonClick={this.includeVolumeRangeDiscount} title="Inserir" />
                                    </Grid>

                                    <Grid item md={12}>
                                        <Box width='99%'>
                                            <EditableTable
                                                {...this.props}
                                                id='idvolumefaixa'
                                                allowEdit
                                                noEditButton
                                                height='50vh'
                                                data={this.state.volumeRangeDiscountList}
                                                columns={this.state.volumeRangeDiscountColumns}
                                                rowId='idvolumefaixa'
                                                totalSize={this.state.volumeRangeDiscountTotalSize}
                                                onPageChange={this.searchVolumeDiscountInfo}
                                                onEditRow={this.onVolumeRangeDiscountTableEdit}
                                                onRowDoubleClick={() => { }}
                                                isLoading={this.state.isLoadingVolumeRangeDiscounteTable}
                                                extraColumnsConfig={
                                                    {
                                                        
                                                        'vlcomprasate': {
                                                            'type': 'number',
                                                        },
                                                        'perdesconto': {
                                                            'type': 'percent',
                                                        },
                                                        'vlcomprasde': {
                                                            'type': 'number',
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
                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.volumeDiscount, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabRange = (event) => {
        handleChangeText(this.state.volumeRangeDiscount, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includeVolumeRangeDiscount = () => {
        if (!this.state.volumeRangeDiscount.vlcomprasde ||
            !this.state.volumeRangeDiscount.vlcomprasate ||
            !this.state.volumeRangeDiscount.perdesconto
        ) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*).',
                alertType: 'error',
                showAlert: true
            })
            return
        }

        const volumeRangeDiscount = {
            ...this.state.volumeRangeDiscount,
            vlcomprasde: this.state.volumeRangeDiscount.vlcomprasde.replace(',', '.'),
            vlcomprasate: this.state.volumeRangeDiscount.vlcomprasate.replace(',', '.'),
        }

        let config = {
            method: 'post',
            endpoint: 'discount/volume/single'
        }
        let form = {
            id: this.state.selectedRow.idvolume,
            volumeRangeDiscount: volumeRangeDiscount,
            type: 'addRange'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    volumeRangeDiscount: {},
                }, () => this.searchVolumeDiscountInfo(0))
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
            volumeDiscount: {},
            volumeRangeDiscount: {},
            volumeRangeDiscountList: [],
            volumeRangeDiscountColumns: {},
            volumeRangeDiscountTotalSize: '',
            isLoadingTab: true,
            isLoadingVolumeRangeDiscountTable: true,
            isANewVolumeDiscount: false
        })
    }

    onVolumeDiscountTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/volume/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            code: this.state.code,
            isCurrent: this.state.isCurrent,
            isExpired: this.state.isExpired
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    volumeDiscountList: r.data.volume_discount,
                    volumeDiscountColumns: r.data.columns,
                    volumeDiscountTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingVolumeDiscountTable: false,
                })
            }
        })
    }

    onVolumeRangeDiscountTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                volumeRangeDiscountList: row
            }, () => this.deleteVolumeRangeDiscount(extraParam))
        }
    }

    saveOrUpdateVolumeDiscount = () => {
        if (!this.state.volumeDiscount.desvolume || !this.state.volumeDiscount.situacao) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (%)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'discount/volume/single'
        }
        let form = {
            id: this.state.volumeDiscount.idvolume,
            volumeDiscount: this.state.volumeDiscount,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewVolumeDiscount) {
                    newState['isANewVolumeDiscount'] = false
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

    searchVolumeDiscountInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/volume/single'
        }
        let form = {
            id: this.state.selectedRow.idvolume,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    volumeDiscount: r.data.volume_discount,

                    volumeRangeDiscountList: r.data.volume_range_discount,
                    volumeRangeDiscountColumns: r.data.columns,
                    volumeRangeDiscountTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingVolumeRangeDiscounteTable: false,
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
                    <Header {...this.props} title='Desconto Volume' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '40px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '10% 40% 17% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} type='number' id='code' value={this.state.code} label='Código' handleChange={this.handleChangeText} width='100%' />
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

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onVolumeDiscountTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ code: '', search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewVolumeDiscount: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idvolume'
                            allowEdit
                            noDeleteButton
                            data={this.state.volumeDiscountList}
                            columns={this.state.volumeDiscountColumns}
                            rowId='idvolume'
                            totalSize={this.state.volumeDiscountTotalSize}
                            onPageChange={this.onVolumeDiscountTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingVolumeDiscountTable}
                            extraColumnsConfig={
                                {
                                    'idvolume': {
                                        'type': 'number'
                                    },
                                    'datainicial': {
                                        'type': 'date'
                                    },
                                    'datafinal': {
                                        'type': 'date'
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

export default VolumeDiscount;