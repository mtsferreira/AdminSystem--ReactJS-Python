import React from "react";

import { Box, Grid } from "@mui/material";
import { Draggable } from "react-beautiful-dnd";
import { formatDate } from "../../utils/datetime";
import { formatPhone, formatValueAsReal } from "../../utils/helpers";

class Task extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
        }
    }

    backgroundColorChange = (props) => {
        return props.isDragging ? 'green' : props.isDraggable ? props.isBacklog ? '#f2d7d5' : '#dcdcdc' : props.isBacklog ? '#f2d7d5' : '#fffada' 
    }

    render() {
        return(
            <Draggable Draggable draggableId={this.props.task.idpedido_id.toString()} key={this.props.task.idpedido_id.toString()} index={this.props.index}>
                {(provided, snapshot) => (
                    <div
                        {...provided.draggableProps}
                        {...provided.dragHandleProps}
                        ref={provided.innerRef}
                        isDragging={snapshot.isDragging}
                    >
                        <Box
                            sx={{
                                border: `1px solid ${this.props.colors.grey[800]}`,
                                borderRadius: '10px',
                                padding: '8px',
                                color: '#000',
                                margin: '0 10px 10px 8px',
                                minHeight: '90px',
                                cursor: 'pointer',
                                display: 'flex',
                                justifyContent: 'space-between',
                                flexDirection: 'column',
                                // backgroundColor: `${(props) => this.backgroundColorChange(props)}}`
                                backgroundColor: 'white'
                            }}
                        >
                            <Grid container columnSpacing={1} rowSpacing={2}>
                                <Grid item md={3}><b>{this.props.task.nrpedido}</b></Grid>
                                <Grid item md={5}><b>{formatDate(this.props.task.dtorcamento)}</b></Grid>
                                <Grid item md={4}><b>{formatValueAsReal(this.props.task.vlorcamento)}</b></Grid>
                                <Grid item md={12}>{this.props.task.razao}</Grid>
                                <Grid item md={6}>{this.props.task.contato}</Grid>
                                <Grid item md={6}>{formatPhone(this.props.task.telefone)}</Grid>
                            </Grid>
                        </Box>
                    </div>
                )}
            </Draggable>
        )
    }

}

export default Task