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


class CustomerTypeDiscount extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingOptions: true,
            isLoadingCustomerTypeDiscountTable: true,
            isLoadingCustomerTypeDiscountStructureTable: true,

            menuId: '23',

            search: null,
            isCurrent: false,
            isExpired: false,

            isANewCustomerTypeDiscount: false,

            customerTypeDiscount: {},
            customerTypeDiscountList: [],
            customerTypeDiscountColumns: {},
            customerTypeDiscountTotalSize: '',

            customerTypeDiscountStructureList: [],
            customerTypeDiscountStructureColumns: {},
            customerTypeDiscountStructureTotalSize: '',

            customerTypeDiscountStructure: {
                idproduto: null,
                idfamilia: null,
                idgrupo: null,
                idggrupo: null,
                idsgrupo: null,
                idmarca: null,
                idcategoria: null,
                idfabricante: null,
                idlinha: null,
                desconto: null,
            },

            tabs: [
                { id: 'data', title: 'Cadastro de tipo de cliente' },
            ],
        }
    }

    closeEditTab = () => {
        var element = document.getElementById('edit-tab')
        element.parentNode.removeChild(element)
        this.onCustomerTypeDiscountTableChange(0)
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onCustomerTypeDiscountTableChange(0)
        optionsRequest(this, ['bigGroup', 'brand', 'category', 'customerType', 'family', 'group', 'manufacturer', 'product', 'productLine', 'subGroup'])
    }

    createEditTab = (params, isRegister = false) => {
        if (isRegister) {
            this.setState({
                selectedRow: params,
                isLoadingTab: true,
                activeTab: 'data',
                customerTypeDiscount: {
                    dtinicial: dayjs().format('YYYY-MM-DD'),
                    dtfinal: dayjs().format('YYYY-MM-DD'),
                },
            }, () => createEditTab('Desconto por Tipo Cliente', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        } else {
            this.setState({
                isANewCustomerTypeDiscount: false,
                selectedRow: params,
                activeTab: 'data',
            }, () => createEditTab('Desconto por Tipo Cliente', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
        }
    }

    deleteCustomerTypeDiscount = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'discount/customer/search'
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
                }, () => this.onCustomerTypeDiscountTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    deleteCustomerTypeDiscountStructure = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'discount/customer/single'
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
                }, () => this.searchCustomerTypeDiscountInfo(0))
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
        if (this.state.isLoadingTab && !this.state.isANewCustomerTypeDiscount) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchCustomerTypeDiscountInfo(0))
            return
        }
        if (!this.state.customerTypeDiscount && !this.state.isANewCustomerTypeDiscount) {
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
                                    <Grid item md={1}><MainTextField {...this.props} type='number' id='iddescontotipo' value={this.state.customerTypeDiscount.iddescontotipo} label='Código' handleChange={this.handleChangeTextTab} disabled='true' /></Grid>
                                    <Grid item md={5}><MainSelectInput required {...this.props} id='tipocliente' value={this.state.customerTypeDiscount.tipocliente} optionsList={this.state.customerTypeOptions} label='Tipo de Cliente' handleChange={this.handleChangeTextTab} width={{ xs: '94%', sm: '94%', md: '100%' }} /></Grid>

                                    <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='dtinicial' value={this.state.customerTypeDiscount.dtinicial} handleChange={this.handleChangeTextTab} type='date' /></Grid>
                                    <Grid item md={2}><MainDateTimeInput onlyDate {...this.props} id='dtfinal' value={this.state.customerTypeDiscount.dtfinal} handleChange={this.handleChangeTextTab} type='date' /></Grid>

                                    <Grid item md={2}>
                                        <MainTabButton width='95%' {...this.props} onButtonClick={this.saveOrUpdateCustomerTypeDiscount} title="Salvar" />
                                    </Grid>
                                </Grid>
                            </Box>
                        </Grid>

                        {!this.state.isANewCustomerTypeDiscount ?
                            <>
                                <Grid item xs={12} sm={12} md={12}><MainSelectInput required {...this.props} id='idproduto' value={this.state.customerTypeDiscountStructure.idproduto || ''} optionsList={this.state.productOptions} label='Produto' handleChange={this.handleChangeTextTabSelects} width={{ xs: '97%', sm: '97%', md: '99%' }} /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idfamilia' value={this.state.customerTypeDiscountStructure.idfamilia || ''} optionsList={this.state.familyOptions} label='Família' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idggrupo' value={this.state.customerTypeDiscountStructure.idggrupo || ''} optionsList={this.state.bigGroupOptions} label='Grande Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idgrupo' value={this.state.customerTypeDiscountStructure.idgrupo || ''} optionsList={this.state.groupOptions} label='Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idsgrupo' value={this.state.customerTypeDiscountStructure.idsgrupo || ''} optionsList={this.state.subGroupOptions} label='Sub Grupo' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idmarca' value={this.state.customerTypeDiscountStructure.idmarca || ''} optionsList={this.state.brandOptions} label='Marca' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idcategoria' value={this.state.customerTypeDiscountStructure.idcategoria || ''} optionsList={this.state.categoryOptions} label='Categoria' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={8}><MainSelectInput {...this.props} id='idfabricante' value={this.state.customerTypeDiscountStructure.idfabricante || ''} optionsList={this.state.manufacturerOptions} label='Fabricante' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={4}><MainSelectInput {...this.props} id='idlinha' value={this.state.customerTypeDiscountStructure.idlinha || ''} optionsList={this.state.productLineOptions} label='Linha' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>
                                <Grid item xs={12} sm={12} md={2}><MainTextField required {...this.props} type='percent' id='desconto' value={this.state.customerTypeDiscountStructure.desconto || ''} label='Desconto (%)' handleChange={this.handleChangeTextTabSelects} fullWidth /></Grid>

                                <Grid item xs={12} sm={12} md={8}></Grid>

                                <Grid item xs={12} sm={12} md={2}>
                                    <MainTabButton sx={{width: { xs: '97%', sm: '97%', md: '94%'}}} {...this.props} onButtonClick={this.includeCustomerTypeDiscountStructure} title="Inserir" />
                                </Grid>

                                <Grid item xs={12} sm={12} md={12} sx={{ width: '100%' }}>
                                    <Box width='99%'>
                                        <EditableTable
                                            {...this.props}
                                            id='iddescontotipoestrutura'
                                            allowEdit
                                            noEditButton
                                            height='50vh'
                                            data={this.state.customerTypeDiscountStructureList}
                                            columns={this.state.customerTypeDiscountStructureColumns}
                                            rowId='iddescontotipoestrutura'
                                            totalSize={this.state.customerTypeDiscountStructureTotalSize}
                                            onPageChange={this.searchCustomerTypeDiscountInfo}
                                            onEditRow={this.oncustomerTypeDiscountStructureTableEdit}
                                            onRowDoubleClick={() => { }}
                                            isLoading={this.state.isLoadingCustomerTypeDiscountStructureTable}
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
                                                    'desconto': {
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
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.customerTypeDiscount, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeTextTabSelects = (event) => {
        handleChangeText(this.state.customerTypeDiscountStructure, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    includeCustomerTypeDiscountStructure = () => {
        if (!this.state.customerTypeDiscountStructure.idproduto) {
            this.setState({
                alertMessage: 'Necessário selecionar um produto.',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        if (!this.state.customerTypeDiscountStructure.desconto) {
            this.setState({
                alertMessage: 'Necessário preencher o Desconto (%).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'discount/customer/single'
        }
        let form = {
            id: this.state.selectedRow.iddescontotipo,
            customerTypeDiscountStructure: this.state.customerTypeDiscountStructure,
            type: 'addStructure'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    customerTypeDiscountStructure: {},
                }, () => this.searchCustomerTypeDiscountInfo(0))
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
            customerTypeDiscount: {},
            customerTypeDiscountStructure: {},
            customerTypeDiscountStructureList: [],
            customerTypeDiscountStructureColumns: {},
            customerTypeDiscountStructureTotalSize: '',
            isLoadingTab: true,
            isLoadingCustomerTypeDiscountStructureTable: true,
            isANewCustomerTypeDiscount: false
        })
    }

    oncustomerTypeDiscountStructureTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                customerTypeDiscountStructureList: row
            }, () => this.deleteCustomerTypeDiscountStructure(extraParam))
        }
    }

    onCustomerTypeDiscountTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/customer/search'
        }
        let form = {
            page: page,
            search: this.state.search,
            isCurrent: this.state.isCurrent,
            isExpired: this.state.isExpired
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerTypeDiscountList: r.data.customer_type_discount,
                    customerTypeDiscountColumns: r.data.columns,
                    customerTypeDiscountTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingCustomerTypeDiscountTable: false
                })
            }
        })
    }

    onCustomerTypeDiscountTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                customerTypeDiscountList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deleteCustomerTypeDiscount(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    saveOrUpdateCustomerTypeDiscount = () => {
        if (!this.state.customerTypeDiscount.tipocliente) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*)',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'discount/customer/single'
        }
        let form = {
            id: this.state.customerTypeDiscount.iddescontotipo,
            customerTypeDiscount: this.state.customerTypeDiscount,
            type: 'updateOrCreate'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                var newState = {
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }

                if (this.state.isANewCustomerTypeDiscount) {
                    newState['isANewCustomerTypeDiscount'] = false
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

    searchCustomerTypeDiscountInfo = (page) => {
        let config = {
            method: 'get',
            endpoint: 'discount/customer/single'
        }
        let form = {
            id: this.state.selectedRow.iddescontotipo,
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    customerTypeDiscount: r.data.customer_type_discount,

                    customerTypeDiscountStructureList: r.data.customer_type_discount_structure,
                    customerTypeDiscountStructureColumns: r.data.columns,
                    customerTypeDiscountStructureTotalSize: r.data.total_size,

                    isLoadingTab: false,
                    isLoadingCustomerTypeDiscountStructureTable: false,
                }, () => this.handleChangeTab())
            }
        })
    }


    render() {
        if (this.state.isLoading || this.state.isLoadingOptions) {
            return (
                <></>
            )
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Desconto por Tipo Cliente' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '50% 17% 10% 10% 10%',
                                },
                            }}
                        >
                            <MainSelectInput {...this.props} id='search' value={this.state.search} optionsList={this.state.customerTypeOptions} label='Tipo de Cliente' handleChange={this.handleChangeText} width='100%' />
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
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onCustomerTypeDiscountTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ search: null, isCurrent: false, isExpired: false })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ isANewCustomerTypeDiscount: true }, (params) => this.createEditTab(params, true))}>Novo</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='iddescontotipo'
                            allowEdit
                            data={this.state.customerTypeDiscountList}
                            columns={this.state.customerTypeDiscountColumns}
                            rowId='iddescontotipo'
                            totalSize={this.state.customerTypeDiscountTotalSize}
                            onPageChange={this.onCustomerTypeDiscountTableChange}
                            onEditRow={this.onCustomerTypeDiscountTableEdit}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingCustomerTypeDiscountTable}
                            extraColumnsConfig={
                                {
                                    'iddescontotipo': {
                                        'type': 'number'
                                    },
                                    'tipocliente_id': {
                                        'type': 'select',
                                        'options': this.state.customerTypeOptions
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

export default CustomerTypeDiscount;