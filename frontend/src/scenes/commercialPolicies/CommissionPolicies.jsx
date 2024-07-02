import React from "react";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess } from "../../utils/layout";
import { Box, Button } from "@mui/material";
import { defaultRequest } from "../../utils/request/request";


class CommissionPolicies extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingCommissionPoliciesTable: true,

            menuId: '18',

            isNewCommissionPolicy: false,

            code: '',
            search: '',
            status: 'A',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Cancelado' },
                { 'value': 'B', 'label': 'Bloqueado' },
            ],

            commissionPoliciesList: [],
            commissionPoliciesColumns: {},
            commissionPoliciesTotalSize: '',
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onCommissionPoliciesTableChange(0)
    }

    handleChangeText = (event) => {
        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    includeCommissionPolicy = () => {
        if (!this.state.description ||
            !this.state.commissionWallet ||
            !this.state.commissionNews ||
            !this.state.situation
        ) {
            this.setState({
                alertMessage: 'Preencha todos os campos obrigatórios (*).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'financial/commissionpolicies'
        }
        let form = {
            infos: {
                despolitica: this.state.description,
                percomissao: this.state.commissionWallet,
                percomnovos: this.state.commissionNews,
                situacao: this.state.situation,
            },
            type: 'Include'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isNewCommissionPolicy: false,
                }, () => this.onCommissionPoliciesTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    onCommissionPoliciesTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'financial/commissionpolicies'
        }
        let form = {
            page: page,
            code: this.state.code,
            term: this.state.search,
            status: this.state.status,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    commissionPoliciesList: r.data.commission_policies,
                    commissionPoliciesColumns: r.data.columns,
                    commissionPoliciesTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingCommissionPoliciesTable: false
                })
            }
        })
    }

    onCommissionPoliciesTableEdit = (row, method, extraParam) => {
        if (method === 'edit') {
            this.setState({
                commissionPoliciesList: row
            }, () => this.saveComissionPolicies(extraParam))
        }
    }

    saveComissionPolicies = (row) => {
        let config = {
            method: 'post',
            endpoint: 'financial/commissionpolicies'
        }
        let form = {
            id: row.idpolcomissao,
            infos: {
                ...row, 
                percomissao: row.percomissao.toString().replace(',', '.'),
                percomnovos: row.percomnovos.toString().replace(',', '.')
            },
            type: 'Edit'
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState(({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isLoadingCommissionPoliciesTable: true
                }), () => this.onCommissionPoliciesTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                }, () => this.onCommissionPoliciesTableChange(0))
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
                    <Header {...this.props} title='Políticas de Comissões' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        <Box
                            sx={{
                                mr: '75px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '10% 45% 15% 10% 10% 10%'
                                },
                            }}
                        >
                            <MainTextField {...this.props} type='number' id='code' value={this.state.code} label='Código' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} id='search' value={this.state.search} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.onCommissionPoliciesTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' onClick={() => this.setState({ status: 'A', search: '', code: '' })}>Limpar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.setState({ isNewCommissionPolicy: !this.state.isNewCommissionPolicy, description: '', commissionWallet: '', commissionNews: '', situation: 'A' })}>{!this.state.isNewCommissionPolicy ? 'Novo' : 'Cancelar'}</Button>
                        </Box>

                        {this.state.isNewCommissionPolicy ?
                            <>
                                <Box className='outline-box'>
                                    <MainLabel sx={{ marginTop: '30px' }} {...this.props} variant="tabTitle" label="Cadastrar nova região de venda" />
                                    <Box
                                        sx={{
                                            mr: '20px',
                                            display: 'grid',
                                            gap: '10px',
                                            gridTemplateColumns: {
                                                md: '100%',
                                                lg: '42% 17% 17% 13% 10%',
                                            },
                                        }}
                                    >
                                        <MainTextField required {...this.props} id='description' value={this.state.description} label='Descrição da Política' handleChange={this.handleChangeText} width={{ xs: '97%', md: '97%', lg: '99%' }} />
                                        <MainTextField required {...this.props} type='percent' id='commissionWallet' value={this.state.commissionWallet} label='Comissão Carteira (%)' handleChange={this.handleChangeText} width={{ xs: '97%', md: '97%', lg: '99%' }} />
                                        <MainTextField required {...this.props} type='percent' id='commissionNews' value={this.state.commissionNews} label='Comissão Novos (%)' handleChange={this.handleChangeText} width={{ xs: '97%', md: '97%', lg: '99%' }} />
                                        <MainSelectInput required {...this.props} id='situation' value={this.state.situation} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width={{ xs: '97%', md: '97%', lg: '99%' }} />

                                        <MainTabButton sx={{ width: { xs: '97%', md: '97%', lg: '95%' } }} {...this.props} onButtonClick={this.includeCommissionPolicy} title="Salvar" />
                                    </Box>
                                </Box>
                            </>
                            :
                            <>
                            </>
                        }

                        <EditableTable
                            {...this.props}
                            id='idpolcomissao'
                            allowEdit
                            allowEditOnRow
                            noDeleteButton
                            noAddRow
                            data={this.state.commissionPoliciesList}
                            columns={this.state.commissionPoliciesColumns}
                            rowId='idpolcomissao'
                            totalSize={this.state.commissionPoliciesTotalSize}
                            onPageChange={this.onCommissionPoliciesTableChange}
                            onEditRow={this.onCommissionPoliciesTableEdit}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingCommissionPoliciesTable}
                            extraColumnsConfig={
                                {
                                    'percomissao': {
                                        'type': 'percent'
                                    },
                                    'percomnovos': {
                                        'type': 'percent'
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
                                    },
                                    'idpolcomissao': {
                                        'disabled': true,
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

export default CommissionPolicies;