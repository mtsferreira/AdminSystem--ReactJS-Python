import React from "react";

import Header from "../../components/Header";
import Kanban from "../../components/kanban/Kanban";

import { Box } from "@mui/material";

class WorkFlowBudget extends React.Component {

    render() {
        return(
            <Box className='outline-box'>
                <Header {...this.props} title='Worflow de Orçamentos' />
                <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                    <Kanban {...this.props} />
                </Box>
            </Box>
        )
    }
}

export default WorkFlowBudget