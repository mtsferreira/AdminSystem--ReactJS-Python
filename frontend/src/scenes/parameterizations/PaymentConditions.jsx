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


class PaymentConditions extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,

            isLoading: true,
            isLoadingPaymentTable: true,

            menuId: '26',
            isANewPaymentCondition: false,

            term: '',
            status: 'A',

            paymentList: [],
            paymentColumns: {},
            paymentTotalSize: '',

            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'B', 'label': 'Bloqueado' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onPaymentTableChange(0)
    }

    deletePayment = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'payment/single'
        }
        let form = {
            id: id,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState(({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isLoadingPaymentTable: true
                }), () => this.onPaymentTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    includePaymentTerm = () => {
        if (!this.state.codeerp ||
            !this.state.description ||
            !this.state.termdays ||
            !this.state.installments ||
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
            endpoint: 'payment'
        }
        let form = {
            infos: {
                coderp: this.state.codeerp,
                descpagamento: this.state.description,
                prazodias: this.state.termdays,
                qparcela: this.state.installments,
                situacao: this.state.situation,
            },
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isANewPaymentCondition: false,
                }, () => this.onPaymentTableChange(0))
            }  else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    onPaymentTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'payment'
        }
        let form = {
            page: page,
            term: this.state.term,
            status: this.state.status
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    paymentList: r.data.payment,
                    paymentColumns: r.data.columns,
                    paymentTotalSize: r.data.total_size,
                    isLoading: false,
                    isLoadingPaymentTable: false
                })
            }
        })
    }

    onPaymentTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                paymentList: row
            }, () => this.deletePayment(extraParam))
        } else if (method === 'edit') {
            this.setState({
                paymentList: row
            }, () => this.savePayment(extraParam))
        }
    }

    savePayment = (row) => {
        let config = {
            method: 'post',
            endpoint: 'payment/single'
        }
        let form = {
            id: row.idpagamento,
            infos: row
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState(({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isLoadingPaymentTable: true
                }), () => this.onPaymentTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                }, () => this.onPaymentTableChange(0))
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
                    <Header {...this.props} title='Condições de Pagamento' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Pesquisar Dados" />
                        {/* SEARCHING FIELDS */}
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '55% 15% 15% 15%',
                                },
                            }}
                        >
                            <MainTextField {...this.props} id='term' value={this.state.term || ''} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput {...this.props} id='status' value={this.state.status || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.onPaymentTableChange(0)}>Buscar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} variant='contained' onClick={() => this.setState({ isANewPaymentCondition: !this.state.isANewPaymentCondition, codeerp: '', description: '', termdays: '', installments: '', situation: 'A' })}>{!this.state.isANewPaymentCondition ? 'Novo' : 'Cancelar'}</Button>
                        </Box>

                        {this.state.isANewPaymentCondition ?
                            <>
                                <Box className='outline-box'>
                                    <MainLabel sx={{ marginTop: '30px' }} {...this.props} variant="tabTitle" label="Cadastrar nova região de venda" />
                                    <Box
                                        sx={{
                                            mr: '40px',
                                            display: 'grid',
                                            gap: '10px',
                                            gridTemplateColumns: {
                                                md: '100%',
                                                lg: '11% 40% 13% 13% 13% 10%',
                                            },
                                        }}
                                    >
                                        <MainTextField required {...this.props} type='number' id='codeerp' value={this.state.codeerp} label='Código ERP' handleChange={this.handleChangeText} width='100%' />
                                        <MainTextField required {...this.props} id='description' value={this.state.description} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                                        <MainTextField required {...this.props} type='number' id='termdays' value={this.state.termdays} label='Prazo Médio' handleChange={this.handleChangeText} width='100%' />
                                        <MainTextField required {...this.props} type='number' id='installments' value={this.state.installments} label='Qtd. Parcelas' handleChange={this.handleChangeText} width='100%' />
                                        <MainSelectInput required {...this.props} id='situation' value={this.state.situation} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                                        <MainTabButton sx={{ width: { xs: '100%', md: '100%', lg: '95%' } }} {...this.props} onButtonClick={this.includePaymentTerm} title="Salvar" />
                                    </Box>
                                </Box>
                            </>
                            :
                            <>
                            </>
                        }

                        <EditableTable
                            {...this.props}
                            allowEdit
                            allowEditOnRow
                            noAddRow
                            id='idpagamento'
                            data={this.state.paymentList}
                            columns={this.state.paymentColumns}
                            rowId='idpagamento'
                            totalSize={this.state.paymentTotalSize}
                            onPageChange={this.onPaymentTableChange}
                            onEditRow={this.onPaymentTableEdit}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingPaymentTable}
                            extraColumnsConfig={
                                {
                                    'coderp': {
                                        'type': 'number',
                                    },
                                    'prazodias': {
                                        'type': 'number',
                                    },
                                    'qparcela': {
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

export default PaymentConditions;