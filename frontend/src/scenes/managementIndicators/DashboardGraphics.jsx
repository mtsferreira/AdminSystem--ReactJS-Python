import React from "react";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

import { addLastAccess } from "../../utils/layout";
import { Box, Button, Grid, Typography } from "@mui/material";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class DashboardGraphics extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            alertType: '',
            alertMessage: '',
            showAlert: false,
            menuId: '2',

            isLoading: true,
            isLoadingGrouperTable: true,

            grouper: {},
            grouperList: [],
            grouperColumns: {},
            grouperTotalSize: '',

            graphicTypeOptions: [],
            graphicGrouperOptions: [],
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Inativo' }
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        optionsRequest(this, ['graphicType', 'graphicGrouper'])
        this.onGrouperTableChange(0)
    }

    deleteTableRow = (grouperId) => {
        let config = {
            method: 'delete',
            endpoint: 'graphics/grouper'
        }

        let form = {
            id: grouperId
        }

        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true
                }, () => this.onGrouperTableChange(0))
            }
        })
    }

    handleChangeText = (event) => {
        handleChangeText(this.state.grouper, event.target.id, event.target.value, () => this.setState({ menuId: '2' }))
    }

    onGrouperTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                grouperList: row
            }, () => this.deleteTableRow(extraParam))
        }
    }

    onGrouperTableChange = (page) => {
        this.setState({ isLoadingGrouperTable: true })
        let config = {
            method: 'get',
            endpoint: 'graphics/grouper'
        }
        let form = {
            page: page
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    grouperList: r.data.groupers,
                    grouperColumns: r.data.columns,
                    grouperTotalSize: r.data.total_size,
                    isLoadingGrouperTable: false,
                    isLoading: false
                })
            }
        })
    }

    saveGrouper = () => {
        let config = {
            method: 'post',
            endpoint: 'graphics/grouper'
        }
        let form = {
            grouper: this.state.grouper
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertType: 'success',
                    alertMessage: r.data.message,
                    showAlert: true,
                    grouper: {}
                }, () => this.onGrouperTableChange(0))
            } else {
                this.setState({
                    alertType: 'error',
                    alertMessage: r.data.message,
                    showAlert: true,
                })
            }
        })
    }


    render() {
        if (this.state.isLoading) {
            return <></>
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Dashboard de Gráficos' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Cadastrar Agrupador" />
                        <Box sx={{ flexGrow: 1 }}>
                            <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }}}>
                                <Grid item md={4}><MainTextField required {...this.props} id='titulo' value={this.state.grouper.titulo} label='Título' handleChange={this.handleChangeText} fullWidth /></Grid>
                                <Grid item md={6}><MainTextField required {...this.props} id='descricao' value={this.state.grouper.descricao} label='Descrição' handleChange={this.handleChangeText} fullWidth /></Grid>
                                <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.grouper.situacao} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} fullWidth /></Grid>

                                <Grid item md={2}><MainSelectInput required {...this.props} id='iddashtipografico' value={this.state.grouper.iddashtipografico} optionsList={this.state.graphicTypeOptions} label='Tipo do Gráfico' handleChange={this.handleChangeText} fullWidth /></Grid>
                                <Grid item md={3}><MainSelectInput required {...this.props} id='iddashgrafico_grupo' value={this.state.grouper.iddashgrafico_grupo} optionsList={this.state.graphicGrouperOptions} label='Agrupador de Gráficos' handleChange={this.handleChangeText} fullWidth /></Grid>
                                
                                <Grid item md={5}></Grid>
                                
                                <Grid item md={2}>
                                    <Button sx={{ width: '98%', height: '40px', backgroundColor: this.props.colors.custom['searchButtons'] }} onClick={this.saveGrouper}>
                                        <Typography sx={{ color: this.props.colors.custom['colorWhite'] }}>
                                            Salvar
                                        </Typography>
                                    </Button>
                                </Grid>
                            </Grid>
                        </Box>
                        <EditableTable
                            {...this.props}
                            id='representedTable'
                            allowEdit
                            noEditButton
                            data={this.state.grouperList}
                            columns={this.state.grouperColumns}
                            rowId={'iddashgrafico'}
                            totalSize={this.state.grouperTotalSize}
                            onPageChange={this.onGrouperTableChange}
                            onEditRow={this.onGrouperTableEdit}
                            onRowDoubleClick={() => { }}
                            isLoading={this.state.isLoadingGrouperTable}
                            extraColumnsConfig={
                                {
                                    'iddashtipografico_id': {
                                        'type': 'select',
                                        'options': this.state.graphicTypeOptions
                                    },
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
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

export default DashboardGraphics