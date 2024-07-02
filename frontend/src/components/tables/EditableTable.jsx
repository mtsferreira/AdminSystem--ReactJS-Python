import React from 'react';

import _ from 'lodash';
import dayjs from 'dayjs';
import MainColorInput from '../inputs/MainColorInput';

// Icons
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/DeleteOutlined';
import SaveIcon from '@mui/icons-material/Save';
import CancelIcon from '@mui/icons-material/Close';

import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { Box, Button, Stack, TextField } from '@mui/material';
import { DatePicker, LocalizationProvider } from '@mui/x-date-pickers';
import { formatDate } from '../../utils/datetime';
import { getNestedProperty } from '../../utils/helpers';
import { GridRowModes, DataGrid, GridToolbarContainer, GridActionsCellItem, GridRowEditStopReasons } from '@mui/x-data-grid';


class CustomDatePicker extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            selectedDate: props.value
        }
    }

    handleChange = (newValue) => {
        this.setState({
            selectedDate: newValue
        })

        const { id, field, api } = this.props
        api.setEditCellValue({ id, field, value: newValue })
    }

    render() {
        return (
            <DatePicker
                value={this.state.selectedDate}
                onChange={this.handleChange}
                renderInput={(params) => <TextField {...params} />}
                format="DD/MM/YYYY"
            />
        )
    }
}

class EditToolbar extends React.Component {
    constructor(props) {
        super(props)
    }

    handleClick = () => {
        // const id = this.props.randomId()
        const id = '------'

        let newRow = {}

        this.props.columns.map((value, index) => {
            if (value[0] !== this.props.rowId) {
                newRow[value[0]] = ''
            } else {
                newRow[value[0]] = id
            }

        })
        this.props.setRows([newRow, ...this.props.oldRows], id)
    };

    render() {
        if (!this.props.noAddRow) {
            console.log(this.props.colors)
            return (
                <GridToolbarContainer>
                    <Button sx={{ mb: '5px', color: 'white', backgroundColor: '#EA5C11', ':hover': { backgroundColor: '#EA5C11' } }} onClick={this.handleClick}>
                        Adicionar Linha
                    </Button>
                </GridToolbarContainer>
            )
        }
        return (
            <></>
        )
    }
}


class EditableTable extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            rows: this.props.data,
            columns: [],
            rowModesModel: {},
            paginationModel: { page: 0, pageSize: 10 },
            page: 0,
            isLoaded: false
        }
    }

    componentWillMount() {
        this.createColumns()
    }

    componentDidUpdate(prevProps) {
        if (this.state.rows !== this.props.data) {
            this.setState({
                rows: this.props.data
            })
        }
        if (prevProps.columns !== this.props.columns) {
            this.setState({
                isLoaded: false
            }, () => this.createColumns())
        }
    }

    calculateColumnWidths(columns, rows) {
        return columns.map(column => {
            let maxWidth = 0
            maxWidth = Math.max(maxWidth, this.getTextWidth(column.headerName))

            rows?.forEach(row => {
                const cellValue = getNestedProperty(row, column.field)?.toString()
                maxWidth = Math.max(maxWidth, this.getTextWidth(cellValue))
            })

            return { ...column, minWidth: maxWidth + 15 }
        });
    }

    createColumns = () => {
        let columns = []
        let keys = this.props.columns

        const dateValueGetter = ({ value }) => {
            return value ? dayjs(value) : null;
        }

        keys.map((value, index) => {
            var column = {
                field: value[0],
                headerName: value[1].toUpperCase(),
                cellClassName: value[0] + '-column--cell',
                flex: 1,
                headerAlign: 'left',
                align: 'left',
                editable: this.props.allowEditOnRow ? true : false
            }
            if (this.props.extraColumnsConfig && value[0] in this.props.extraColumnsConfig) {
                let type = this.props.extraColumnsConfig[value[0]]['type']
                if (type === 'date') {
                    column['type'] = 'date'
                    column['valueGetter'] = dateValueGetter
                    column['valueFormatter'] = (params) => formatDate(params?.value)
                    column['renderEditCell'] = (params) => <CustomDatePicker {...params} />
                } else if (type === 'select') {
                    column['type'] = 'singleSelect'
                    column['valueOptions'] = this.props.extraColumnsConfig[value[0]]['options']
                } else if (type === 'number') {
                    column['type'] = 'number'
                    column['align'] = 'right'
                    column['headerAlign'] = 'right'
                } else if (type === 'percent') {
                    column['align'] = 'right';
                    column['headerAlign'] = 'right';
                    column['valueFormatter'] = (params) => {
                        if (params.value != null) {
                            const formattedValue = params.value.toString().replace('.', ',')
                            return `${formattedValue} %`
                        }
                        return ''
                    }
                } else if (type === 'color') {
                    var path = 'params.row.' + value[0]
                    column['renderCell'] = (params) => <div style={{ backgroundColor: eval(path), height: '20PX', width: '20PX', borderRadius: '3px', boxShadow: `2px 2px 3px ${this.props.colors.custom['boxShadow']}` }}  {...params} />
                }
                else if (type === 'colorById') {
                    column['renderCell'] = (params) => {
                        const colorObj = this.props.extraColumnsConfig[value[0]]['options'].find(
                            color => color.value === params.row[value[0]]
                        );

                        const hexColor = colorObj ? colorObj.label : '#FFFFFF';

                        return (
                            <div
                                style={{
                                    backgroundColor: hexColor,
                                    height: '20px',
                                    width: '20px',
                                    borderRadius: '3px',
                                    boxShadow: `2px 2px 3px ${this.props.colors.custom['boxShadow']}`,
                                }}
                            />
                        );
                    };
                }
            } else {
                column['type'] = 'text'
            }
            if (value[0].split('.').length > 1) {
                var path = 'params.row.' + value[0]
                column['valueGetter'] = (params) => { return eval(path) }
            }
            if (this.props.extraColumnsConfig && value[0] in this.props.extraColumnsConfig) {
                if (this.props.extraColumnsConfig[value[0]]['disabled']) {
                    column['editable'] = false
                }
            }
            columns.push(column)
        })

        this.setState({
            columns: this.calculateColumnWidths(columns, this.props.data),
            isLoaded: true
        })
    }

    generateRandom() {
        var length = 8,
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
            retVal = ""
        for (var i = 0, n = charset.length; i < length; ++i) {
            retVal += charset.charAt(Math.floor(Math.random() * n))
        }
        return retVal
    }

    getTextWidth(text) {
        // Criar um elemento canvas para medir o tamanho do texto
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        context.font = '16px Arial'; // Ajuste isso para a fonte que você está usando
        return context.measureText(text).width;
    }

    handleCancelClick = (id) => () => {
        this.setState({
            rowModesModel: {
                ...this.state.rowModesModel,
                [id]: { mode: GridRowModes.View, ignoreModifications: true },
            },
        })

        const editedRow = this.state.rows.find((row) => row[this.props.rowId] === id)
        if (editedRow.isNew) {
            this.setState({
                rows: this.state.rows.filter((row) => row[this.props.rowId] !== id),
            })
        }
    }

    handleDeleteClick = (id) => () => {
        const updatedRows = this.state.rows.filter((row) => row[this.props.rowId] !== id)

        this.setState({
            rows: updatedRows,
        }, () => this.setRowsCallback(updatedRows, 'delete', id))
    }

    handleEditClick = (id) => () => {
        this.setState({
            rowModesModel: { ...this.state.rowModesModel, [id]: { mode: GridRowModes.Edit } },
        })
    }

    handleRowEditStop = (params, event) => {
        if (params.reason === GridRowEditStopReasons.rowFocusOut) {
            event.defaultMuiPrevented = true;
        }
    }

    handleRowModesModelChange = (newRowModesModel) => {
        this.setState({ rowModesModel: newRowModesModel })
    }

    handleSaveClick = (id) => () => {
        this.setState({
            rowModesModel: { ...this.state.rowModesModel, [id]: { mode: GridRowModes.View } },
        })
    }

    onPageChange = (newPage) => {
        this.setState({ paginationModel: { ...this.state.paginationModel, page: newPage.page } }, () => this.props.onPageChange(this.state.paginationModel.page))
    }

    processRowUpdate = (newRow) => {
        const updatedRow = { ...newRow, isNew: false }
        this.setState({
            rows: this.state.rows.map((row) => (row[this.props.rowId] === newRow[this.props.rowId] ? updatedRow : row)),
        }, () => this.setRowsCallback(this.state.rows, 'edit', newRow))
        return updatedRow
    }

    setRows = (rows, id) => {
        this.setState({
            rows: rows
        }, this.setRowsCallback(rows[0], 'add'))
    }

    setRowsCallback = (rows, method, extraParam = null) => {
        this.props.onEditRow(rows, method, extraParam)
    }

    setRowModesModel = (models) => {
        this.setState({
            rowModesModel: models
        })
    }

    render() {
        var appendedColumns = this.state.columns
        if (this.props.allowEdit) {
            appendedColumns = [
                ...this.state.columns,
                {
                    field: 'actions',
                    type: 'actions',
                    headerName: 'AÇÕES',
                    width: 100,
                    cellClassName: 'actions',
                    getActions: ({ id, row }) => {
                        const isInEditMode = this.state.rowModesModel[id]?.mode === GridRowModes.Edit

                        if (isInEditMode) {
                            return [
                                <GridActionsCellItem
                                    icon={<SaveIcon />}
                                    label="Save"
                                    onClick={this.handleSaveClick(id)}
                                    sx={{ "& .MuiSvgIcon-root": { 'color': this.props.colors.primary[100] } }}
                                />,
                                <GridActionsCellItem
                                    icon={<CancelIcon />}
                                    label="Cancel"
                                    className="textPrimary"
                                    onClick={this.handleCancelClick(id)}
                                    sx={{ "& .MuiSvgIcon-root": { 'color': this.props.colors.primary[100] } }}
                                />,
                            ]
                        }

                        var buttonList = []

                        if (!this.props.noEditButton) {
                            if (this.props.allowEditOnRow) {
                                buttonList.push(
                                    <GridActionsCellItem
                                        icon={<EditIcon />}
                                        label="Edit"
                                        className="textPrimary"
                                        onClick={this.handleEditClick(id)}
                                        sx={{ "& .MuiSvgIcon-root": { 'color': this.props.colors.primary[100] } }}
                                    />
                                )
                            } else {
                                buttonList.push(
                                    <GridActionsCellItem
                                        icon={<EditIcon />}
                                        label="Edit"
                                        className="textPrimary"
                                        onClick={() => {
                                            row['id'] = row[this.props.rowId]
                                            this.props.onRowDoubleClick(row)
                                        }}
                                        sx={{ "& .MuiSvgIcon-root": { 'color': this.props.colors.primary[100] } }}
                                    />
                                )
                            }
                        }
                        if (!this.props.noDeleteButton) {
                            buttonList.push(
                                <GridActionsCellItem
                                    icon={<DeleteIcon />}
                                    label="Delete"
                                    onClick={this.handleDeleteClick(id)}
                                    sx={{ "& .MuiSvgIcon-root": { color: this.props.colors.primary[100] } }}
                                />
                            )
                        }

                        return buttonList
                    },
                },
            ]
        }

        return (
            <Box
                m={this.props.customMargin ?? '30px 0 0 0'}
                height={this.props.height ?? '75vh'}
                backgroundColor={this.props.colors.primary[400]} // BackgroundColor EditableTable
            >
                <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DataGrid
                        paginationMode="server"
                        editMode="row"
                        loading={this.props.isLoading}
                        sx={{
                            '& .MuiDataGrid-columnHeaders': {
                                backgroundColor: this.props.colors.custom['headerTable'], // Cabeçalho da EditableTable - primary[800]
                                lineHeight: '25px',
                                minHeight: '40px !important',
                                maxHeight: '40px !important',
                            },
                            '& .MuiDataGrid-overlayWrapperInner': {
                                backgroundColor: this.props.colors.primary[400]
                            },
                            '& .MuiDataGrid-columnHeaderTitle': {
                                color: this.props.colors.custom['barsIconsAndTexts'] // Cor somente dos textos do cabeçãlho da EditableTable
                            },
                            '& .MuiTablePagination-root': {
                                color: this.props.colors.primary[100] // totalSize da EditableTable
                            },
                            '& .MuiSvgIcon-root': {
                                color: this.props.colors.primary[100]
                            },
                            color: this.props.colors.primary[100], // Textos do da EditableTable em geral - primary[100]
                            fontSize: '14px',
                            borderColor: this.props.colors.grey[700],
                            '--unstable_DataGrid-overlayBackground': 'transparent',
                            '& .MuiDataGrid-footerContainer': {
                                height: '32px',
                                minHeight: '32px'
                            },
                            ...this.props.sx,
                        }}
                        initialState={{
                            pagination: { paginationModel: { pageSize: 10, page: 0 } }
                        }}
                        slots={{
                            toolbar: this.props.allowEditOnRow ? EditToolbar : null,
                            NoRowsOverlay: () => (
                                <Stack height="100%" alignItems="center" justifyContent="center">
                                    Nenhum Resultado Encontrado
                                </Stack>
                            ),
                            NoResultsOverlay: () => (
                                <Stack height="100%" alignItems="center" justifyContent="center">
                                    Nenhum Resultado Encontrado
                                </Stack>
                            )
                        }}
                        slotProps={{
                            toolbar: {
                                setRows: this.setRows,
                                randomId: this.generateRandom,
                                oldRows: this.state.rows,
                                colors: this.props.colors.custom['secondaryButton'],
                                columns: this.props.columns,
                                noAddRow: this.props.noAddRow,
                                rowId: this.props.rowId
                            },
                        }}
                        columns={appendedColumns}
                        rows={this.state.rows}
                        rowCount={this.props.totalSize}
                        getRowId={(row) => row[this.props.rowId]}
                        processRowUpdate={this.processRowUpdate}
                        rowModesModel={this.state.rowModesModel}
                        onPaginationModelChange={(newPage) => this.onPageChange(newPage)}
                        onRowModesModelChange={this.handleRowModesModelChange}
                        onRowEditStop={this.handleRowEditStop}
                        onRowDoubleClick={(params, event) => { this.props.onRowDoubleClick(params.row, event) }}
                    />
                </LocalizationProvider>
            </Box>
        );
    }
}

export default EditableTable
