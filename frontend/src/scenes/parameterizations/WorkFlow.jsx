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
import { defaultRequest, optionsRequest } from "../../utils/request/request";


class WorkFlow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingOptions: true,
            isLoadingWorkFlowTable: true,

            menuId: '34',
            isNewWorkflow: false,

            workflowId: '',
            workflowColor: '',
            workflowStatus: '',
            workflowDescription: '',
            workflowOrder: '',

            newWorkflowColor: '',
            newWorkflowStatus: '',
            newWorkflowDescription: '',
            newWorkflowOrder: '',

            workflowList: [],
            workflowColumns: {},
            workflowTotalSize: '',

            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'B', 'label': 'Bloqueado' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        optionsRequest(this, ['colorListByHex', 'colorListByName'])
        this.onWorkflowTableChange(0)
    }

    deleteWorkflow = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'workflow/search'
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
                }, () => this.onWorkflowTableChange(0))
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

    includeWorkflow = () => {
        if (!this.state.newWorkflowDescription ||
            !this.state.newWorkflowColor ||
            !this.state.newWorkflowStatus ||
            !this.state.newWorkflowOrder
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
            endpoint: 'workflow/search'
        }
        let form = {
            infos: {
                desworkflow: this.state.newWorkflowDescription,
                idlistacor: this.state.newWorkflowColor,
                situacao: this.state.newWorkflowStatus,
                ordem: this.state.newWorkflowOrder
            }
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    newWorkflowDescription: '',
                    newWorkflowColor: '',
                    newWorkflowStatus: '',
                    newWorkflowOrder: '',
                    isNewWorkflow: false,
                    menuId: 33,
                }, () => this.onWorkflowTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    onWorkflowRowDoubleClick = (params) => {
        this.setState({
            workflowId: params.idworkflow,
            workflowStatus: params.situacao,
            workflowColor: params.idlistacor_id,
            workflowDescription: params.desworkflow,
            workflowOrder: params.ordem
        })
    }

    onWorkflowTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'workflow/search'
        }
        let form = {
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    workflowList: r.data.workflow,
                    workflowColumns: r.data.columns,
                    workflowTotalSize: r.data.total_size,
                    isLoading: false,
                    isLoadingWorkflowTable: false
                })
            }
        })
    }

    onWorkflowTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                workflowList: row // Atualiza a lista, sem a linha que foi excluída
            }, () => this.deleteWorkflow(extraParam)) // extraParam = Id da linha que foi excluída
        }
    }

    saveWorkflow = () => {
        let config = {
            method: 'post',
            endpoint: 'workflow/single'
        }
        let form = {
            id: this.state.workflowId,
            workflow: {
                idworkflow: this.state.workflowId,
                desworkflow: this.state.workflowDescription,
                situacao: this.state.workflowStatus,
                ordem: this.state.workflowOrder,
                idlistacor: this.state.workflowColor
            }
        }
        if (!this.state.workflowDescription || !this.state.workflowStatus || !this.state.workflowColor || !this.state.workflowId || !this.state.workflowOrder) {
            this.setState({
                alertMessage: 'Workflow inválido',
                alertType: 'error',
                showAlert: true
            })
        } else {
            defaultRequest(config, form).then((r) => {
                if (r.status) {
                    this.setState(({
                        alertMessage: r.data.message,
                        alertType: 'success',
                        showAlert: true,

                        workflowColor: this.state.workflowColor,
                        workflowDescription: this.state.workflowDescription,
                        workflowStatus: this.state.workflowStatus,
                        workflowOrder: this.state.workflowOrder
                    }), () => this.onWorkflowTableChange(0))
                } else {
                    this.setState({
                        alertMessage: r.data.message,
                        alertType: 'error',
                        showAlert: true
                    })
                }
            })
        }
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
                    <Header {...this.props} title='WorkFlow' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubSubTitle" label="Selecione um WorkFlow" />
                        <Box
                            sx={{
                                mr: '90px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '7% 35% 10% 15% 13% 10% 10%',
                                },
                                marginTop: '25px'
                            }}
                        >
                            <MainTextField {...this.props} id='workflowId' value={this.state.workflowId || ''} label='Código' handleChange={this.handleChangeText} disabled='true' width='100%' />
                            <MainTextField {...this.props} id='workflowDescription' value={this.state.workflowDescription || ''} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainTextField {...this.props} type='number' id='workflowOrder' value={this.state.workflowOrder || ''} label='Ordem' handleChange={this.handleChangeText} width='100%' />

                            <MainSelectInput {...this.props} id='workflowColor' value={this.state.workflowColor} optionsList={this.state.colorListByNameOptions} label='Cor' handleChange={this.handleChangeText} width='100%'
                                sx={{
                                    '& fieldset': {
                                        borderColor: this.state.workflowColor ? this.state.colorListByHexOptions.find(color => color.value === this.state.workflowColor)?.label : this.props.colors.grey[1100], // borda do input
                                    },
                                    '& .MuiOutlinedInput-root': {
                                        '&.Mui-focused fieldset': {
                                            borderColor: this.state.workflowColor ? this.state.colorListByHexOptions.find(color => color.value === this.state.workflowColor)?.label : this.props.colors.grey[1100], // borda do input quando está selecionado
                                        },
                                    },
                                    '& label.Mui-focused': {
                                        color: this.props.colors.grey[1100], // cor do label quando o input está selecionado
                                    },
                                }}
                            />

                            <MainSelectInput {...this.props} id='workflowStatus' value={this.state.workflowStatus || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'], width: '100%' }} variant='contained' onClick={this.saveWorkflow}>Salvar</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'], width: '100%' }} variant='contained' onClick={() => this.setState({ isNewWorkflow: true })}>Novo</Button>
                        </Box>

                        {this.state.isNewWorkflow ?
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
                                                lg: '40% 10% 15% 13% 10% 10%',
                                            },
                                        }}
                                    >
                                        <MainTextField required {...this.props} id='newWorkflowDescription' value={this.state.newWorkflowDescription || ''} label='Descrição' handleChange={this.handleChangeText} width='98%' />
                                        <MainTextField required {...this.props} type='number' id='newWorkflowOrder' value={this.state.newWorkflowOrder || ''} label='Ordem' handleChange={this.handleChangeText} width='98%' />

                                        <MainSelectInput required {...this.props} id='newWorkflowColor' value={this.state.newWorkflowColor} optionsList={this.state.colorListByNameOptions} label='Cor' handleChange={this.handleChangeText} width='98%'
                                            sx={{
                                                '& fieldset': {
                                                    borderColor: this.state.newWorkflowColor ? this.state.colorListByHexOptions.find(color => color.value === this.state.newWorkflowColor)?.label : this.props.colors.grey[1100], // borda do input
                                                },
                                                '& .MuiOutlinedInput-root': {
                                                    '&.Mui-focused fieldset': {
                                                        borderColor: this.state.newWorkflowColor ? this.state.colorListByHexOptions.find(color => color.value === this.state.newWorkflowColor)?.label : this.props.colors.grey[1100], // borda do input quando está selecionado
                                                    },
                                                },
                                                '& label.Mui-focused': {
                                                    color: this.props.colors.grey[1100], // cor do label quando o input está selecionado
                                                },
                                            }}
                                        />

                                        <MainSelectInput required {...this.props} id='newWorkflowStatus' value={this.state.newWorkflowStatus || ''} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='98%' />

                                        <MainTabButton sx={{ width: '98%' }} {...this.props} onButtonClick={this.includeWorkflow} title="Salvar" />
                                        <MainTabButton sx={{ width: '98%' }} {...this.props} onButtonClick={() => this.setState({ isNewWorkflow: false, newWorkflowDescription: '', newWorkflowColor: '', newWorkflowStatus: '', newWorkflowOrder: '' })} title="Cancelar" />

                                    </Box>
                                </Box>
                            </>
                            :
                            <></>
                        }

                        <EditableTable
                            {...this.props}
                            allowEdit
                            noEditButton
                            id='idworkflow'
                            data={this.state.workflowList}
                            columns={this.state.workflowColumns}
                            rowId={'idworkflow'}
                            totalSize={this.state.workflowTotalSize}
                            onPageChange={this.onWorkflowTableChange}
                            onEditRow={this.onWorkflowTableEdit}
                            onRowDoubleClick={(params) => this.onWorkflowRowDoubleClick(params)}
                            isLoading={this.state.isLoadingWorkflowTable}
                            extraColumnsConfig={
                                {
                                    'idworkflow': {
                                        'type': 'number',
                                    },
                                    'ordem': {
                                        'type': 'number',
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
                                    },
                                    'idlistacor_id': {
                                        'type': 'colorById',
                                        'options': this.state.colorListByHexOptions
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

export default WorkFlow;