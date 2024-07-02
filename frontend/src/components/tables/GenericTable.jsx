import React from "react";

import { Box, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../typograhpy";

import { mockData } from "../../data/mockData";

function withHooks(WrappedComponent) {
    return function(props) {
        const theme = useTheme()
        const colors = tokens(theme.palette.mode)
        
        return (
            < WrappedComponent colors={colors} theme={theme} {...props} />
        )
    }
}

class GenericTable extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoaded: false
        }
    }

    componentWillMount() {
        this.createColumns()
    }

    createColumns = () => {
        let keys = Object.keys(this.props.data[0])

        let columns = []
        keys.map((value, index) => {
            columns.push({
                field: value, 
                headerName: value.toUpperCase(), 
                cellClassName: value+'-column--cell',
                type: 'number' ? typeof value == 'number' : 'text',
                flex: value != 'id' ? 1 : 0,
                headerAlign: 'center',
                align: 'center'
            })
        })

        if (this.props.extraColumnsConfig) {
            columns.push(this.props.extraColumnsConfig)
        }

        this.setState({
            columns: columns,
            isLoaded: true
        })
    }
    
    render() {
        if (!this.state.isLoaded) {
            return <></>
        }
        return (
            <Box
                m='30px 0 0 0'
                height='75vh'
                backgroundColor={this.props.colors.primary[400]}
            >
                <DataGrid 
                    rows={this.props.data}
                    columns={this.state.columns}
                    onRowDoubleClick={this.props.onDoubleClick ? (event) => this.props.onDoubleClick(event.row) : undefined}
                    sx={{
                        '& .MuiDataGrid-columnHeaders': {
                            backgroundColor: this.props.colors.primary[800],
                            lineHeight:'30px'
                        }
                    }}
                />
            </Box>
        )
    }
}

export default withHooks(GenericTable)