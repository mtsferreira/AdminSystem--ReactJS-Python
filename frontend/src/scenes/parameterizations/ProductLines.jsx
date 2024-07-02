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
import { Box, Button, Grid, Typography } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class ProductLines extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingProductLinesTable: true,
            isLoadingProductLinesSpecificationTable: true,

            menuId: '29',
            isANewProductLine: false,
            newProductLinesDescription: '',
            newProductLinesStructure: '',
            newProductLinesStatus: '',

            productLines: {},
            productLinesList: [],
            productLinesColumns: {},
            productLinesTotalSize: '',

            productLinesStructureList: [],
            productLinesStructureColumns: {},
            productLinesStructureTotalSize: '',

            productLinesStructure: {
                familia: null,
                grupo: null,
                ggrupo: null,
                sgrupo: null,
                marca: null,
                categoria: null,
                fabricante: null,
            },

            search: '',
            status: 'A',
            productLinesCode: '',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'B', 'label': 'Bloqueado' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],
            structureOptions: [
                { 'value': 'S', 'label': 'Somente os produtos relacionados' },
                { 'value': 'N', 'label': 'Todos os prosutos, exceto os relacionados' },
            ],
            tabs: [
                { id: 'data', title: 'Especificação da Linha de Produto' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onProductLinesTableChange(0)
        optionsRequest(this, ['bigGroup', 'brand', 'category', 'family', 'group', 'manufacturer', 'subGroup'])
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
        }, () => createEditTab('Produto', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deleteProductLinesStructure = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'product/lines/single'
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
                }, () => this.searchProductLinesInfo(0))
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
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchProductLinesInfo(0))
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={2}><MainTextField {...this.props} type='number' id='idlinha' value={this.state.productLines.idlinha} label='Código' handleChange={this.handleChangeTextTab} disabled='true' fullWidth /></Grid>
                        <Grid item md={10}><MainTextField required {...this.props} id='deslinha' value={this.state.productLines.deslinha} label='Descrição da Linha' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={6}><MainSelectInput required {...this.props} id='estrutura' value={this.state.productLines.estrutura} optionsList={this.state.structureOptions} label='Estrutura' handleChange={this.handleChangeTextTab} fullWidth /></Grid>
                        <Grid item md={3}><MainSelectInput required {...this.props} id='situacao' value={this.state.productLines.situacao} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} fullWidth /></Grid>

                        <Grid item md={3}>
                            <MainTabButton sx={{width: { xs: '97%', sm: '97%', md: '89%'}}} {...this.props} onButtonClick={this.updateProductLines} title="Salvar" />
                        </Grid>
                    </Grid>

                    <MainLabel {...this.props} variant="tabSubSubTitle" label="Estrutura da Linha de Produto" />
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={4}><MainSelectInput {...this.props} id='familia' value={this.state.productLinesStructure.familia || ''} optionsList={this.state.familyOptions} label='Família' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='ggrupo' value={this.state.productLinesStructure.ggrupo || ''} optionsList={this.state.bigGroupOptions} label='Grande Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='grupo' value={this.state.productLinesStructure.grupo || ''} optionsList={this.state.groupOptions} label='Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='sgrupo' value={this.state.productLinesStructure.sgrupo || ''} optionsList={this.state.subGroupOptions} label='Sub Grupo' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='marca' value={this.state.productLinesStructure.marca || ''} optionsList={this.state.brandOptions} label='Marca' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={4}><MainSelectInput {...this.props} id='categoria' value={this.state.productLinesStructure.categoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextTabSelects} /></Grid>
                        <Grid item md={8}><MainSelectInput {...this.props} id='fabricante' value={this.state.productLinesStructure.fabricante || ''} optionsList={this.state.manufacturerOptions} label='Fabricante' handleChange={this.handleChangeTextTabSelects} width={{ xs: '94%', sm: '94%', md: '97%' }} /></Grid>

                        <Grid item md={4}>
                            <MainTabButton width='94%' {...this.props} onButtonClick={this.includeProductLinesStructure} title="Inserir" />
                        </Grid>
                    </Grid>

                    <Box
                        margin='0 10px 0 10px'
                    >
                        <EditableTable
                            {...this.props}
                            allowEdit
                            noEditButton
                            height='50vh'
                            id='productLinesStructureTable'
                            data={this.state.productLinesStructureList}
                            columns={this.state.productLinesStructureColumns}
                            rowId='idestrutura'
                            totalSize={this.state.productLinesStructureTotalSize}
                            onPageChange={this.searchProductLinesInfo}
                            onEditRow={this.onProductLinesStructureTableEdit}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingProductLinesSpecificationTable}
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
                                    }
                                }
                            }
                        />
                    </Box>
                </Box>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.productLines, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabSelects = (event) => {
        handleChangeText(this.state.productLinesStructure, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includeProductLinesStructure = () => {
        if (!this.state.productLinesStructure.familia &&
            !this.state.productLinesStructure.ggrupo &&
            !this.state.productLinesStructure.grupo &&
            !this.state.productLinesStructure.sgrupo &&
            !this.state.productLinesStructure.marca &&
            !this.state.productLinesStructure.categoria &&
            !this.state.productLinesStructure.fabricante
        ) {
            this.setState({
                alertMessage: 'Necessário selecionar, no mínimo, uma das opções.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'product/lines/single'
        }
        let form = {
            id: this.state.selectedRow.idlinha,
            productLinesStructure: this.state.productLinesStructure,
            type: 'addProductLinesStructure'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                }, () => this.searchProductLinesInfo(0))
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
            activeTab: 'data',
            isLoadingTab: true,
            isLoadingProductLinesSpecificationTable: true,
            productLines: {},
            productLinesStructure: {},
        })
    }

    onProductLinesStructureTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                productLinesStructureList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deleteProductLinesStructure(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    onProductLinesTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/lines/search'
        }
        let form = {
            page: page,
            search: this.state.search,
            productLinesCode: this.state.productLinesCode,
            status: this.state.status
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productLinesList: r.data.product_lines,
                    productLinesColumns: r.data.columns,
                    productLinesTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingProductLinesTable: false,
                })
            }
        })
    }

    saveProductLines = () => {
        if (!this.state.newProductLinesDescription || !this.state.newProductLinesStructure || !this.state.newProductLinesStatus) {
            this.setState({
                alertMessage: 'Descrição|Estrutura|Situação Inválido',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'product/lines/search'
        }
        let form = {
            infos: {
                deslinha: this.state.newProductLinesDescription,
                estrutura: this.state.newProductLinesStructure,
                situacao: this.state.newProductLinesStatus
            }
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    newProductLinesDescription: '',
                    newProductLinesStructure: '',
                    newProductLinesStatus: '',
                    menuId: 29
                }, () => this.onProductLinesTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    searchProductLinesInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'product/lines/single'
        }
        let form = {
            id: this.state.selectedRow.idlinha,
            page: page,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    productLines: r.data.product_lines,
                    productLinesStructureList: r.data.product_lines_structure,
                    productLinesStructureColumns: r.data.columns,
                    productLinesStructureTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingProductLinesSpecificationTable: false,
                }, () => this.handleChangeTab())
            }
        })
    }

    updateProductLines = () => {
        let config = {
            method: 'post',
            endpoint: 'product/lines/single'
        }
        let form = {
            id: this.state.selectedRow.idlinha,
            productLines: this.state.productLines,
            type: 'updateProductLine'
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
                    <Header {...this.props} title='Linhas de Produto' menuId={this.state.menuId} showFav />
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
                            <MainTextField {...this.props} type='number' id='productLinesCode' value={this.state.productLinesCode} label='Código' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onProductLinesTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ productLinesCode: '', search: '', status: 'A' })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewProductLine: true })}>Novo</Button>
                        </Box>

                        {this.state.isANewProductLine ?
                            <>
                                <Box margin='30px 0 0 0'>
                                    <MainLabel sx={{ marginTop: '30px' }} {...this.props} variant="tabSubSubTitle" label="Cadastrar nova linha de produto" />

                                    <Box
                                        mr='25px'
                                        mt='30px'
                                        display='grid'
                                        gap='8px'
                                        gridTemplateColumns='32% 32% 13% 11.5% 11.5%'
                                    >
                                        <MainTextField {...this.props} id='newProductLinesDescription' value={this.state.newProductLinesDescription} label='Descrição da Linha' handleChange={this.handleChangeText} fullWidth />
                                        <MainSelectInput {...this.props} id='newProductLinesStructure' value={this.state.newProductLinesStructure} optionsList={this.state.structureOptions} label='Estrutura' handleChange={this.handleChangeText} fullWidth />
                                        <MainSelectInput {...this.props} id='newProductLinesStatus' value={this.state.newProductLinesStatus} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} />

                                        <Box
                                            display='flex'
                                            justifyContent='center'
                                            borderRadius='4px'
                                            backgroundColor={this.props.colors.custom['secondaryButton']}
                                            onClick={this.saveProductLines}
                                            height='100%'
                                            width='95%'
                                        >
                                            <Button sx={{ width: '100%' }}><Typography sx={{ color: this.props.colors.custom['colorWhite'], fontWeight: '600', letterSpacing: '3px', fontSize: '12px' }}>Salvar</Typography></Button>
                                        </Box>


                                        <Box
                                            display='flex'
                                            justifyContent='center'
                                            borderRadius='4px'
                                            backgroundColor={this.props.colors.custom['secondaryButton']}
                                            onClick={() => this.setState({ isANewProductLine: false, newProductLinesDescription: '', newProductLinesStructure: '', newProductLinesStatus: '' })}
                                            height='100%'
                                            width='95%'
                                        >
                                            <Button sx={{ width: '100%' }}><Typography sx={{ color: this.props.colors.custom['colorWhite'], fontWeight: '600', fontSize: '12px', letterSpacing: '3px' }}>Cancelar</Typography></Button>
                                        </Box>

                                    </Box>
                                </Box>
                            </>
                            : <></>}

                        <EditableTable
                            {...this.props}
                            id='productLinesTable'
                            allowEdit
                            noDeleteButton
                            data={this.state.productLinesList}
                            columns={this.state.productLinesColumns}
                            rowId='idlinha'
                            totalSize={this.state.productLinesTotalSize}
                            onPageChange={this.onProductLinesTableChange}
                            onEditRow={() => { }}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingProductLinesTable}
                            extraColumnsConfig={
                                {
                                    'idlinha': {
                                        'type': 'number',
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
                                    },
                                    'estrutura': {
                                        'type': 'select',
                                        'options': this.state.structureOptions
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

export default ProductLines;