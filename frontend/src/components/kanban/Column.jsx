import React from "react";

import Task from "./Task";

import { Box } from "@mui/material";
import { Droppable } from "react-beautiful-dnd";

class Column extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
        }
    }

    render() {
        return(
            <Box 
                sx={{
                    backgroundColor: this.props.colors.custom['colorWhite'],
                    borderRadius: '6px',
                    margin: '8px',
                    minWidth: '320px',
                    width: '320px',
                    height: '575px',
                    border: `2px solid ${this.props.color}`,
                    boxShadow: `3px 3px 3px ${this.props.colors.custom['boxShadow']}`
                }}
            >
                <h4 style={{padding: '8px', margin: '0'}}>{this.props.title}</h4>

                <Box className='scrollable-element'>
                    <Droppable droppableId={this.props.id} key={this.props.id}>

                        {(provided, snapshot) => (
                            <div
                                {...provided.droppableProps}
                                ref={provided.innerRef}
                                isDraggingOver={snapshot.isDraggingOver}
                            >
                                <Box
                                    sx={{
                                        minHeight: '550px',
                                        margin:'0 8px',
                                        transition: 'background-color 0.2s ease',
                                        display: 'flex',
                                        flexGrow: '1',
                                        flexDirection: 'column',
                                    }}                                
                                >
                                    {this.props.taskList.map((task, index) => {
                                        return (
                                            <Task {...this.props} key={index} index={index} task={task} />
                                        )
                                    })}
                                    {provided.placeholder}
                                </Box>
                            </div>
                        )}

                    </Droppable>
                </Box>
            </Box>
        )
    }

}

export default Column