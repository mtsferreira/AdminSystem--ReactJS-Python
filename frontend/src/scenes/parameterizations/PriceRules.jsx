import React from "react";
import ReactDOM from "react-dom";

import dayjs from 'dayjs';
import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainDateTimeInput from "../../components/inputs/MainDateTimeInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid, Typography } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class PriceRules extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingPriceRulesTable: true,

            menuId: '31',

            search: '',
            isCurrent: false,
            isExpired: false,
            priceRulesCode: '',
            isANewPriceRules: false,

            priceRules: {},
            priceRulesList: [],
            priceRulesColumns: {},
            priceRulesTotalSize: '',

            tabs: [
                { id: 'data', title: 'Regra de Preço' },
            ],

        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onPriceRulesTableChange(0)
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onPriceRulesTableChange(0)
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                priceRules: {
                    datainicial: dayjs().format('YYYY-MM-DD'),
                    datafinal: dayjs().format('YYYY-MM-DD'),
                    ipi: false,
                    st: false,
                    pis: false,
                    cofins: false,
                    icms: false,
                }
            }, () => createEditTab('Formação de Regras de Preço', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewPriceRules: false,
                selectedRow: params,
                isLoadingTab: true,
            }, () => createEditTab('Criação de Regras de Preço', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab && !this.state.isANewPriceRules) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchPriceRulesInfo())
            return
        }
        if (!this.state.priceRules && !this.state.isANewPriceRules) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={2}><MainTextField {...this.props} type='number' id='idprecoregra' value={this.state.priceRules.idprecoregra} label='Código' handleChange={this.handleChangeTextTab} disabled='true' fullWidth /></Grid>
                        <Grid item md={10}><MainTextField required {...this.props} id='desregra' value={this.state.priceRules.desregra} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '97%', sm: '97%', md: '98.5%' }} /></Grid>

                        <Grid item md={2}><MainTextField required {...this.props} type='percent' id='peracrescimo' value={this.state.priceRules.peracrescimo} label='Acréscimo (%)' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainTextField required {...this.props} type='percent' id='perdesconto' value={this.state.priceRules.perdesconto} label='Redução (%)' handleChange={this.handleChangeTextTab} fullWidth /></Grid>

                        <Grid item md={3} sx={{ marginLeft: { sm: '0', md: '68px' }}} ><MainDateTimeInput {...this.props} onlyDate id='datainicial' value={this.state.priceRules.datainicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                        <Box
                            display='flex'
                            justifyContent='center'
                            alignItems='center'
                            paddingTop='15px'
                            marginRight='5px'
                        >
                            <span>até</span>
                        </Box>
                        <Grid item md={3}><MainDateTimeInput {...this.props} onlyDate id='datafinal' value={this.state.priceRules.datafinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>


                        <Grid item md={3}><MainCheckBoxInput {...this.props} id='ipi' value={this.state.priceRules.ipi} label='Acréscimo IPI' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={3}><MainCheckBoxInput {...this.props} id='st' value={this.state.priceRules.st} label='Acréscimo ST' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={3}><MainCheckBoxInput {...this.props} id='pis' value={this.state.priceRules.pis} label='Acréscimo PIS' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={3}><MainCheckBoxInput {...this.props} id='cofins' value={this.state.priceRules.cofins} label='Acréscimo COFINS' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={3}><MainCheckBoxInput {...this.props} id='icms' value={this.state.priceRules.icms} label='Acréscimo ICMS' handleChange={this.handleChangeTextTab} /></Grid>
                        <Grid item md={6}></Grid>


                        <Grid item md={3}>
                            <MainTabButton width='93%' {...this.props} onButtonClick={this.saveOrUpdatePriceRules} title="Salvar" />
                        </Grid>

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

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.priceRules, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingTab: true,
            priceRules: {},
        })
    }

    onPriceRulesTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'price/rules'
        }
        let form = {
            page: page,
            term: this.state.search,
            priceRulesCode: this.state.priceRulesCode,
            isCurrent: this.state.isCurrent,
            isExpired: this.state.isExpired
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    priceRulesList: r.data.price_rules,
                    priceRulesColumns: r.data.columns,
                    priceRulesTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingPriceRulesTable: false,
                })
            }
        })
    }

    saveOrUpdatePriceRules = () => {
        let config = {
            method: 'post',
            endpoint: 'price/rules/single'
        }
        let form = {
            id: this.state.priceRules.idprecoregra,
            priceRules: this.state.priceRules,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewPriceRules) {
                    newState['isANewPriceRules'] = false
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

    searchPriceRulesInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'price/rules/single'
        }
        let form = {
            id: this.state.selectedRow.idprecoregra
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var priceRulesSingle = r.data.price_rules
                priceRulesSingle.ipi = priceRulesSingle.ipi === 'S'
                priceRulesSingle.st = priceRulesSingle.st === 'S'
                priceRulesSingle.pis = priceRulesSingle.pis === 'S'
                priceRulesSingle.cofins = priceRulesSingle.cofins === 'S'
                priceRulesSingle.icms = priceRulesSingle.icms === 'S'

                this.setState({
                    priceRules: priceRulesSingle,

                    isLoadingTab: false,
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
                    <Header {...this.props} title='Regras de Preço' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '10% 40% 17% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} type='number' id='priceRulesCode' value={this.state.priceRulesCode} label='Código' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Mensagem' handleChange={this.handleChangeText} width='100%' />
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
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onPriceRulesTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ priceRulesCode: '', search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewPriceRules: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idprice'
                            allowEdit
                            noDeleteButton
                            data={this.state.priceRulesList}
                            columns={this.state.priceRulesColumns}
                            rowId='idprecoregra'
                            totalSize={this.state.priceRulesTotalSize}
                            onPageChange={this.onPriceRulesTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingPriceRulesTable}
                            extraColumnsConfig={
                                {
                                    'idprecoregra': {
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
                </Box>
            </>
        )
    }
}

export default PriceRules;