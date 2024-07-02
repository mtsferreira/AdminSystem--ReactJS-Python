import React from "react";

import Column from "./Column";
import dayjs from "dayjs";
import LoadingGif from "../visual/LoadingGif";
import MainDateTimeInput from "../inputs/MainDateTimeInput";
import MainSelectInput from "../inputs/MainSelectInput";

import { Box, Button, Grid } from "@mui/material";
import { DragDropContext } from "react-beautiful-dnd";
import { defaultRequest } from "../../utils/request/request";
import { optionsRequest } from "../../utils/request/request";

class Kanban extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            menuId: '11',
            columns: [

            ],
            isLoaded: false,
            completed: [
                {
                    id: '1',
                    content: 'Texto 1',
                    completed: true
                },
                {
                    id: '3',
                    content: 'Texto 3',
                    completed: true
                }
            ],
            incomplete: [
                {
                    id: '2',
                    content: 'Texto 2',
                    completed: false
                }
            ],
            inReview: [],
            backlog: [],

            initialDate: dayjs('2023-01-01').format('YYYY-MM-DD'),
            finalDate: dayjs().format('YYYY-MM-DD'),
            localSale: '',
            localSaleOptions: []
        }
    }

    componentDidMount() {
        optionsRequest(this, ['localSale'])
        let config = {
            endpoint: 'workflow/search',
            method: 'get'
        }
        let form = {
            noPagination: true
        }
        defaultRequest(config, form).then((r) => {
            if(r.status) {
                var columns = [
                    {
                        id: '9999',
                        title: 'SEM WORKFLOW',
                        color: '#ffffff',
                        taskList: []
                    }
                ]
                r.data.workflow.forEach((value, index) => {
                    columns.push({
                        id: value.idworkflow.toString(),
                        title: value.desworkflow,
                        color: value.cor.cor,
                        taskList: []
                    })
                })
                this.setState({columns: columns, isLoaded: true})
            }
        })
    }

    clearKanban = () => {
        const newColumns = this.state.columns.map(column => ({
            ...column,
            taskList: []
          }))
      
          this.setState({ columns: newColumns, isLoaded: false }, ()=>this.searchWorkflowOrders())
    }

    editOrderWorkflow = (taskId, workflowId) => {
        let config = {
            endpoint: 'workflow/order',
            method: 'post'
        }
        let form = {
            id: taskId,
            workflowId: workflowId
        }
        defaultRequest(config, form)
    }

    handleChangeText = (event) => {
        this.setState({
            [event.target.id]: event.target.value,
        })
    }

    handleDragEnd = (result) => {
        const { destination, source, draggableId } = result
        
        if (!destination || source.droppableId === destination.droppableId) return
        
        const task = this.findItemById(draggableId)
        this.deletePreviousState(source.droppableId, draggableId, destination.droppableId, task)
        this.editOrderWorkflow(task.idpedido_id, destination.droppableId)
    }
        
    deletePreviousState = (sourceDroppableId, taskId, destinationDroppableId, task) => {
        const newColumns = this.state.columns.map(column => {
            if (column.id === sourceDroppableId) {
                const filteredTasks = column.taskList.filter(task => task.idpedido_id.toString() !== taskId)
                return { ...column, taskList: filteredTasks }
            }
            return column
        })
        this.setState({ columns: newColumns }, ()=>this.setNewState(destinationDroppableId, task))
    }
    
    setNewState = (destinationDroppableId, task) => {
        const newColumns = this.state.columns.map(column => {
            if (column.id === destinationDroppableId) {
                const newTaskList = [...column.taskList, task]
                return { ...column, taskList: newTaskList }
            }
            return column
        })
        
        this.setState({ columns: newColumns })
    }
      
    findItemById = (id) => {
        for (const column of this.state.columns) {
            const task = column.taskList.find(task => task.idpedido_id.toString() === id)
            if (task) {
                return task
            }
        }
        return null
    }

    searchWorkflowOrders = () => {
        let config = {
            endpoint: 'workflow/order/search',
            method: 'get'
        }
        let form = {
            initialDate: this.state.initialDate,
            finalDate: this.state.finalDate,
            localSale: this.state.localSale
        }
        defaultRequest(config, form).then((r) => {
            if(r.status) {
                var columns = this.state.columns
                r.data.order.forEach((value, index) => {
                    if (!value.idworkflow_id) {
                        const workflow = columns.find(w => w.id === '9999')
                        if (workflow) {
                            workflow.taskList.push(value)
                        }
                    } else {
                        const workflow = columns.find(w => w.id === value.idworkflow_id.toString())
                        if (workflow) {
                            workflow.taskList.push(value)
                        }
                    }
                })
                this.setState({
                    isLoaded: true,
                    columns: columns
                })
            }
        })
    }

    render() {
        if(!this.state.isLoaded) {
            return <LoadingGif />
        }
        return(
            <DragDropContext onDragEnd={this.handleDragEnd}>
                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', md: 'column', lg: 'row' } }}>
                    <Grid item md={6}><MainSelectInput {...this.props} id='localSale' value={this.state.localSale} optionsList={this.state.localSaleOptions} label='Local de Venda' handleChange={this.handleChangeText} width='100%' /></Grid>
                    <Grid item md={2}><MainDateTimeInput {...this.props} onlyDate id='initialDate' value={this.state.initialDate} handleChange={this.handleChangeText} type='date' width='100%' /></Grid>
                    <Grid item md={2}><MainDateTimeInput {...this.props} onlyDate id='finalDate' value={this.state.finalDate} handleChange={this.handleChangeText} type='date' width='100%' /></Grid>
                    <Grid item md={2}>
                        <Button 
                            sx={{ background: this.props.colors.custom['searchButtons'], width: '100%', height: '100%' }} 
                            {...this.props} 
                            variant='contained' 
                            onClick={() => this.clearKanban()}
                        >
                            Buscar
                        </Button>
                    </Grid>
                </Grid>
                <Box sx={{display: 'flex', justifyContent: 'left', alignItems: 'center', flexDirection: 'row', overflowX: 'auto', marginTop: '20px'}}>
                    {this.state.columns.map((value, index) => {
                        return(
                            <Column {...this.props} id={value.id} title={value.title} taskList={value.taskList} color={value.color} />
                        )
                    })}
                </Box>
            </DragDropContext>
        )
    }

}

export default Kanban