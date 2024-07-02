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
import { defaultRequest, getCityOptionsRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class ShippingCif extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingShippingCifTable: true,
            isLoadingShippingCifLocationTable: true,

            menuId: '24',

            search: '',
            status: 'A',
            isCurrent: false,
            isExpired: false,
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Cancelado' },
                { 'value': 'B', 'label': 'Bloqueado' },
            ],
            isANewShippingCif: false,

            cityOptionsByUfOrigin: [],
            cityOptionsByUfDestiny: [],

            shippingCif: {},
            shippingCifList: [],
            shippingCifColumns: {},
            shippingCifTotalSize: '',

            shippingCifLocationList: [],
            shippingCifLocationColumns: {},
            shippingCifLocationTotalSize: '',

            shippingCifLocation: {
                uforigem: null,
                ufdestino: null,
                codibgeorigem: null,
                codibgedestino: null,
                vlminimo: null,
                peracrescimo: null,
                perdesconto: null,
            },

            tabs: [
                { id: 'data', title: 'Dados Tabela para Frete CIF' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onShippingCifTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onShippingCifTableChange(0)
        optionsRequest(this, ['uf', 'city'])
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                shippingCif: {
                    datainicial: dayjs().format('YYYY-MM-DD'),
                    datafinal: dayjs().format('YYYY-MM-DD'),
                    vlminimo: null,
                    peracrescimo: null,
                    perdesconto: null,
                },
            }, () => createEditTab('Frete CIF', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewShippingCif: false,
                selectedRow: params,
                activeTab: 'data',
            }, () => createEditTab('Frete CIF', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteShippingCifLocation = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'shippingcif/single'
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
                }, () => this.searchShippingCifInfo(0))
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
        if (this.state.isLoadingTab && !this.state.isANewShippingCif) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchShippingCifInfo(0))
            return
        }
        if (!this.state.shippingCif && !this.state.isANewShippingCif) {
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
                                        <Grid item md={2}><MainTextField {...this.props} type='number' id='idfretecif' value={this.state.shippingCif.idfretecif} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                        <Grid item md={10}><MainTextField required {...this.props} id='desfretecif' value={this.state.shippingCif.desfretecif} label='Descrição da Tabela' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '99%' }} /></Grid>

                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datainicial' value={this.state.shippingCif.datainicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datafinal' value={this.state.shippingCif.datafinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>

                                        <Grid item md={2}><MainTextField required {...this.props} type='percent' id='perdesconto1' value={this.state.shippingCif.perdesconto1} label='Desconto 1 (%)' handleChange={this.handleChangeTextTab} /></Grid>
                                        <Grid item md={2}><MainTextField required {...this.props} type='percent' id='perdesconto2' value={this.state.shippingCif.perdesconto2} label='Desconto 2 (%)' handleChange={this.handleChangeTextTab} /></Grid>

                                        <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.shippingCif.situacao} label='situacao' optionsList={this.state.statusOptions} handleChange={this.handleChangeTextTab} /></Grid>

                                        <Grid item md={2}>
                                            <MainTabButton width='95%' {...this.props} onButtonClick={this.saveOrUpdateShippingCif} title="Salvar" />
                                        </Grid>
                                    </Grid>
                                </Box>
                            </Grid>

                            {!this.state.isANewShippingCif ?
                                <>
                                    <Grid item xs={12} sm={12} md={2}><MainSelectInput required {...this.props} id='uforigem' value={this.state.shippingCifLocation.uforigem} label='UF Origem' optionsList={this.state.ufOptions} handleChange={this.handleChangeTextSelectUfOriginTab} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput required {...this.props} id='codibgeorigem' value={this.state.shippingCifLocation.codibgeorigem} label='Cidade Origem' optionsList={this.state.cityOptionsByUfOrigin} handleChange={this.handleChangeTextTabLocation} fullWidth /></Grid>

                                    <Grid item xs={12} sm={12} md={2}><MainSelectInput required {...this.props} id='ufdestino' value={this.state.shippingCifLocation.ufdestino} label='UF Destino' optionsList={this.state.ufOptions} handleChange={this.handleChangeTextSelectUfDestinyTab} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput required {...this.props} id='codibgedestino' value={this.state.shippingCifLocation.codibgedestino} label='Cidade Destino' optionsList={this.state.cityOptionsByUfDestiny} handleChange={this.handleChangeTextTabLocation} fullWidth /></Grid>

                                    <Grid item xs={12} sm={12} md={2}><MainTextField required {...this.props} type='currency' id='vlminimo' value={this.state.shippingCifLocation.vlminimo || ''} label='Vl. Mínimo' handleChange={this.handleChangeTextTabLocation} /></Grid>
                                    <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='percent' id='peracrescimo' value={this.state.shippingCifLocation.peracrescimo || ''} label='Acréscimo (%)' handleChange={this.handleChangeTextTabLocation} /></Grid>
                                    <Grid item xs={12} sm={12} md={2}><MainTextField {...this.props} type='percent' id='perdesconto' value={this.state.shippingCifLocation.perdesconto || ''} label='Desconto (%)' handleChange={this.handleChangeTextTabLocation} /></Grid>

                                    <Grid item xs={12} sm={12} md={4}></Grid>

                                    <Grid item xs={12} sm={12} md={2}>
                                        <MainTabButton width='94%' {...this.props} onButtonClick={this.saveShippingCifLocation} title="Inserir" />
                                    </Grid>

                                    <Grid item xs={12} sm={12} md={12} sx={{ width: '100%' }}>
                                        <Box width='99%'>
                                            <EditableTable
                                                {...this.props}
                                                id='idfreteuf'
                                                allowEdit
                                                noEditButton
                                                height='50vh'
                                                data={this.state.shippingCifLocationList}
                                                columns={this.state.shippingCifLocationColumns}
                                                rowId='idfreteuf'
                                                totalSize={this.state.shippingCifLocationTotalSize}
                                                onPageChange={this.searchShippingCifInfo}
                                                onEditRow={this.onShippingCifLocationTableEdit}
                                                onRowDoubleClick={() => { }}
                                                isLoading={this.state.isLoadingShippingCifLocationTable}
                                                extraColumnsConfig={
                                                    {
                                                        'codibgeorigem_id': {
                                                            'type': 'select',
                                                            'options': this.state.cityOptions
                                                        },
                                                        'codibgedestino_id': {
                                                            'type': 'select',
                                                            'options': this.state.cityOptions
                                                        },
                                                        'vlminimo': {
                                                            'type': 'number',
                                                        },
                                                        'peracrescimo': {
                                                            'type': 'percent',
                                                        },
                                                        'perdesconto': {
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
                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.shippingCif, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabLocation = (event) => {
        handleChangeText(this.state.shippingCifLocation, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeText = (event) => {
        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    handleChangeTextSelectUfDestinyTab = (event) => {
        getCityOptionsRequest(this, event.target.value).then((r) => {
            this.setState(prevState => ({
                cityOptionsByUfDestiny: r.data.city_options,
                shippingCifLocation: { ...prevState.shippingCifLocation, ufdestino: event.target.value }
            }), () => this.handleChangeTab());
        });
    }

    handleChangeTextSelectUfOriginTab = (event) => {
        getCityOptionsRequest(this, event.target.value).then((r) => {
            this.setState(prevState => ({
                cityOptionsByUfOrigin: r.data.city_options,
                shippingCifLocation: { ...prevState.shippingCifLocation, uforigem: event.target.value }
            }), () => this.handleChangeTab());
        });
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingTab: true,
            shippingCif: {},
            shippingCifLocation: {},
            shippingCifLocationList: [],
            shippingCifLocationColumns: {},
            shippingCifLocationTotalSize: '',
            isLoadingTab: true,
            isLoadingShippingCifLocationTable: true,
            isANewShippingCif: false
        })
    }

    onShippingCifLocationTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                shippingCifLocationList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deleteShippingCifLocation(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    onShippingCifTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'shippingcif/search'
        }
        let form = {
            page: page,
            term: this.state.search,
            status: this.state.status,
            isCurrent: this.state.isCurrent,
            isExpired: this.state.isExpired
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    shippingCifList: r.data.shipping_cif,
                    shippingCifColumns: r.data.columns,
                    shippingCifTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingShippingCifTable: false
                })
            }
        })
    }

    saveOrUpdateShippingCif = () => {
        let config = {
            method: 'post',
            endpoint: 'shippingcif/single'
        }
        let form = {
            id: this.state.shippingCif.idfretecif,
            shippingCif: this.state.shippingCif,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewShippingCif) {
                    newState['isANewShippingCif'] = false
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

    saveShippingCifLocation = () => {
        if (
            !this.state.shippingCifLocation.uforigem ||
            !this.state.shippingCifLocation.ufdestino ||
            !this.state.shippingCifLocation.codibgeorigem ||
            !this.state.shippingCifLocation.codibgedestino ||
            !this.state.shippingCifLocation.vlminimo
        ) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*)',
                alertType: 'error',
                showAlert: true
            })
            return
        }

        const shippingCifLocation = {
            ...this.state.shippingCifLocation,
            vlminimo: this.state.shippingCifLocation.vlminimo.replace(',', '.')
        };

        let config = {
            method: 'post',
            endpoint: 'shippingcif/single'
        }
        let form = {
            id: this.state.shippingCif.idfretecif,
            shippingCifLocation: shippingCifLocation,
            type: 'addLocation'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    shippingCifLocation: {},
                    isLoadingTab: true
                }, () => this.searchShippingCifInfo(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    searchShippingCifInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'shippingcif/single'
        }
        let form = {
            id: this.state.selectedRow.idfretecif,
            page: page,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    shippingCif: r.data.shipping_cif,

                    shippingCifLocationList: r.data.shipping_cif_location,
                    shippingCifLocationColumns: r.data.columns,
                    shippingCifLocationTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingShippingCifLocationTable: false,
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
                    <Header {...this.props} title='Frete Cif' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    xl: '35% 15% 17% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />
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
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onShippingCifTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ status: 'A', search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewShippingCif: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idfretecif'
                            allowEdit
                            noDeleteButton
                            data={this.state.shippingCifList}
                            columns={this.state.shippingCifColumns}
                            rowId='idfretecif'
                            totalSize={this.state.shippingCifTotalSize}
                            onPageChange={this.onShippingCifTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingShippingCifTable}
                            extraColumnsConfig={
                                {
                                    'idfretecif': {
                                        'type': 'number'
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
                                    },
                                    'datainicial': {
                                        'type': 'date'
                                    },
                                    'datafinal': {
                                        'type': 'date'
                                    },
                                    'perdesconto1': {
                                        'type': 'percent'
                                    },
                                    'perdesconto2': {
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

export default ShippingCif;