import React from "react";
import {
    GridRowModes,
    GridToolbarColumnsButton,
    GridToolbarContainer,
    GridToolbarDensitySelector,
    GridToolbarExportContainer,
    GridCsvExportMenuItem,
    // GridPrintExportMenuItem,
    GridToolbarFilterButton,
    GridToolbarQuickFilter
} from "@mui/x-data-grid";
// import GridExcelExportMenuItem from "./GridExcelExportMenuItem";
import Button from "@mui/material/Button";
import AddIcon from "@mui/icons-material/Add";

class DefaultToolbar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rows: props.rows,
            columns: props.columns
        };
    }

    createRowData = (rows) => {
        const newId = Math.max(...rows.map((r) => r.id * 1)) + 1;
        return { id: newId };
    };

    handleClick = () => {
        const newData = this.createRowData(this.state.rows);
        newData.isNew = true;
        if (!newData.hasOwnProperty("id"))
            newData.newId = Math.max(...this.state.rows.map((r) => r.id * 1)) + 1;
        this.setState((prevState) => ({
            rows: [...prevState.rows, newData]
        }));
        this.props.setRowModesModel((oldModel) => {
            const firstEditable = this.state.columns.find((c) => c.editable && !c.hide);
            return {
                ...oldModel,
                [newData.id]: { mode: GridRowModes.Edit, fieldToFocus: firstEditable.field }
            };
        });
    };

    render() {
        return (
            <GridToolbarContainer>
                <GridToolbarColumnsButton />
                <GridToolbarFilterButton />
                <GridToolbarDensitySelector />
                <GridToolbarExportContainer>
                    {/* <GridExcelExportMenuItem columns={this.state.columns} /> */}
                    <GridCsvExportMenuItem />
                    {/*<GridPrintExportMenuItem />*/}
                </GridToolbarExportContainer>
                <Button color="primary" startIcon={<AddIcon />} onClick={this.handleClick}>
                    Add record
                </Button>
                <GridToolbarQuickFilter />
            </GridToolbarContainer>
        );
    }
}

DefaultToolbar.defaultProps = {
    createRowData: (rows) => {
        const newId = Math.max(...rows.map((r) => r.id * 1)) + 1;
        return { id: newId };
    }
};

export default DefaultToolbar;
