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


class PriceStructure extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingPriceStructureTable: true,
            isLoadingPriceStructureCompositionTable: true,

            menuId: '20',

            code: '',
            search: '',
            isCurrent: false,
            isExpired: false,
            variationType: [
                { 'value': 'A', 'label': 'Acréscimo' },
                { 'value': 'D', 'label': 'Desconto' },
            ],

            isANewPriceStructure: false,

            priceStructure: {},
            priceStructureList: [],
            priceStructureColumns: {},
            priceStructureTotalSize: '',

            priceStructureComposition: {
                familia: null,
                grupo: null,
                ggrupo: null,
                sgrupo: null,
                marca: null,
                categoria: null,
                fabricante: null,
                origem: null,
                idlinha: null,
                pervariacao: null,
                tipovariacao: null,
            },
            priceStructureCompositionList: [],
            priceStructureCompositionColumns: {},
            priceStructureCompositionTotalSize: '',

            tabs: [
                { id: 'data', title: 'Dados Variações de Preço por Estrutura' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onPriceStructureTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onPriceStructureTableChange(0)
        optionsRequest(this, ['bigGroup', 'brand', 'category', 'family', 'group', 'manufacturer', 'origin', 'product', 'productLine', 'subGroup'])
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                priceStructure: {
                    datainicial: dayjs().format('YYYY-MM-DD'),
                    datafinal: dayjs().format('YYYY-MM-DD'),
                },
            }, () => createEditTab('Preço X Estrutura', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewPriceStructure: false,
                selectedRow: params,
                activeTab: 'data',
            }, () => createEditTab('Preço X Estrutura', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deletePriceStructureComposition = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'price/structure/single'
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
                }, () => this.searchPriceStructureInfo(0))
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
        if (this.state.isLoadingTab && !this.state.isANewPriceStructure) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchPriceStructureInfo(0))
            return
        }
        if (!this.state.priceStructure && !this.state.isANewPriceStructure) {
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
                                        <Grid item md={1}><MainTextField {...this.props} type='number' id='idprecoestrutura' value={this.state.priceStructure.idprecoestrutura} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                        <Grid item md={5}><MainTextField required {...this.props} id='descprecoestrutura' value={this.state.priceStructure.descprecoestrutura} label='Descrição da Variação' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '99%' }} /></Grid>

                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datainicial' value={this.state.priceStructure.datainicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                        <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='datafinal' value={this.state.priceStructure.datafinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>

                                        <Grid item md={2}>
                                            <MainTabButton width='94%' {...this.props} onButtonClick={this.saveOrUpdatePriceStructure} title="Salvar" />
                                        </Grid>
                                    </Grid>
                                </Box>
                            </Grid>

                            {!this.state.isANewPriceStructure ?
                                <>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='familia' value={this.state.priceStructureComposition.familia || ''} optionsList={this.state.familyOptions} label='Família' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='ggrupo' value={this.state.priceStructureComposition.ggrupo || ''} optionsList={this.state.bigGroupOptions} label='Grande Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='grupo' value={this.state.priceStructureComposition.grupo || ''} optionsList={this.state.groupOptions} label='Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='sgrupo' value={this.state.priceStructureComposition.sgrupo || ''} optionsList={this.state.subGroupOptions} label='Sub Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='marca' value={this.state.priceStructureComposition.marca || ''} optionsList={this.state.brandOptions} label='Marca' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='categoria' value={this.state.priceStructureComposition.categoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='fabricante' value={this.state.priceStructureComposition.fabricante || ''} optionsList={this.state.manufacturerOptions} label='Fabricante' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='origem' value={this.state.priceStructureComposition.origem || ''} optionsList={this.state.originOptions} label='Origem' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idlinha' value={this.state.priceStructureComposition.idlinha || ''} optionsList={this.state.productLineOptions} label='Linha' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                    <Grid item xs={12} sm={12} md={2}><MainTextField required {...this.props} type='percent' id='pervariacao' value={this.state.priceStructureComposition.pervariacao || ''} label='Variação (%)' handleChange={this.handleChangeTextTabSelects} /></Grid>
                                    <Grid item xs={12} sm={12} md={2}><MainSelectInput required {...this.props} id='tipovariacao' value={this.state.priceStructureComposition.tipovariacao || ''} optionsList={this.state.variationType} label='Tipo de Variação' handleChange={this.handleChangeTextTabSelects} /></Grid>

                                    <Grid item xs={12} sm={12} md={6}></Grid>

                                    <Grid item xs={12} sm={12} md={2}>
                                        <MainTabButton width='94%' {...this.props} onButtonClick={this.includePriceStructureComposition} title="Inserir" />
                                    </Grid>

                                    <Grid item xs={12} sm={12} md={12} sx={{ width: '100%' }}>
                                        <Box width='99%'>
                                            <EditableTable
                                                {...this.props}
                                                id='idprecofaixa'
                                                allowEdit
                                                noEditButton
                                                height='50vh'
                                                data={this.state.priceStructureCompositionList}
                                                columns={this.state.priceStructureCompositionColumns}
                                                rowId='idprecofaixa'
                                                totalSize={this.state.priceStructureCompositionTotalSize}
                                                onPageChange={this.searchPriceStructureInfo}
                                                onEditRow={this.onPriceStructureCompositionTableEdit}
                                                onRowDoubleClick={() => { }}
                                                isLoading={this.state.isLoadingPriceStructureCompositionTable}
                                                extraColumnsConfig={
                                                    {
                                                        'familia_id': {
                                                            'type': 'select',
                                                            'options': this.state.familyOptions
                                                        },
                                                        'ggrupo_id': {
                                                            'type': 'select',
                                                            'options': this.state.bigGroupOptions
                                                        },
                                                        'grupo_id': {
                                                            'type': 'select',
                                                            'options': this.state.groupOptions
                                                        },
                                                        'sgrupo_id': {
                                                            'type': 'select',
                                                            'options': this.state.subGroupOptions
                                                        },
                                                        'marca_id': {
                                                            'type': 'select',
                                                            'options': this.state.brandOptions
                                                        },
                                                        'categoria_id': {
                                                            'type': 'select',
                                                            'options': this.state.categoryOptions
                                                        },
                                                        'fabricante_id': {
                                                            'type': 'select',
                                                            'options': this.state.manufacturerOptions
                                                        },
                                                        'origem_id': {
                                                            'type': 'select',
                                                            'options': this.state.originOptions
                                                        },
                                                        'idlinha_id': {
                                                            'type': 'select',
                                                            'options': this.state.productLineOptions
                                                        },
                                                        'pervariacao': {
                                                            'type': 'percent',
                                                        },
                                                        'tipovariacao': {
                                                            'type': 'select',
                                                            'options': this.state.variationType
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
        handleChangeText(this.state.priceStructure, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabSelects = (event) => {
        handleChangeText(this.state.priceStructureComposition, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includePriceStructureComposition = () => {
        if (!this.state.priceStructureComposition.pervariacao) {
            this.setState({
                alertMessage: 'Necessário preencher a Variação (%).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        if (!this.state.priceStructureComposition.tipovariacao) {
            this.setState({
                alertMessage: 'Necessário preencher o Tipo de Variação.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        if (!this.state.priceStructureComposition.familia &&
            !this.state.priceStructureComposition.ggrupo &&
            !this.state.priceStructureComposition.grupo &&
            !this.state.priceStructureComposition.sgrupo &&
            !this.state.priceStructureComposition.marca &&
            !this.state.priceStructureComposition.categoria &&
            !this.state.priceStructureComposition.fabricante &&
            !this.state.priceStructureComposition.origem &&
            !this.state.priceStructureComposition.idlinha
        ) {
            this.setState({
                alertMessage: 'Necessário selecionar uma das opções.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'price/structure/single'
        }
        let form = {
            id: this.state.selectedRow.idprecoestrutura,
            priceStructureComposition: this.state.priceStructureComposition,
            type: 'addComposition'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    priceStructureComposition: {},
                }, () => this.searchPriceStructureInfo(0))
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
            priceStructure: {},
            priceStructureComposition: {},
            priceStructureCompositionList: [],
            priceStructureCompositionColumns: {},
            priceStructureCompositionTotalSize: '',
            isLoadingTab: true,
            isLoadingPriceStructureCompositionTable: true,
            isANewPriceStructure: false
        })
    }

    onPriceStructureCompositionTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                priceStructureCompositionList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deletePriceStructureComposition(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    onPriceStructureTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'price/structure/search'
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
                    priceStructureList: r.data.price_structure,
                    priceStructureColumns: r.data.columns,
                    priceStructureTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingPriceStructureTable: false,
                })
            }
        })
    }

    saveOrUpdatePriceStructure = () => {
        if (!this.state.priceStructure.descprecoestrutura) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (%)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'price/structure/single'
        }
        let form = {
            id: this.state.priceStructure.idprecoestrutura,
            priceStructure: this.state.priceStructure,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewPriceStructure) {
                    newState['isANewPriceStructure'] = false
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

    searchPriceStructureInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'price/structure/single'
        }
        let form = {
            id: this.state.selectedRow.idprecoestrutura,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    priceStructure: r.data.price_structure,

                    priceStructureCompositionList: r.data.price_structure_composition,
                    priceStructureCompositionColumns: r.data.columns,
                    priceStructureCompositionTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingPriceStructureCompositionTable: false,
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
                    <Header {...this.props} title='Preço X Estrutura' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '40px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    xl: '10% 40% 17% 10% 10% 10%',
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

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onPriceStructureTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ code: '', search: '', isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewPriceStructure: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idprecoestrutura'
                            allowEdit
                            noDeleteButton
                            data={this.state.priceStructureList}
                            columns={this.state.priceStructureColumns}
                            rowId='idprecoestrutura'
                            totalSize={this.state.priceStructureTotalSize}
                            onPageChange={this.onPriceStructureTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingPriceStructureTable}
                            extraColumnsConfig={
                                {
                                    'idprecoestrutura': {
                                        'type': 'number'
                                    },
                                    'datainicial': {
                                        'type': 'date'
                                    },
                                    'datafinal': {
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

export default PriceStructure;