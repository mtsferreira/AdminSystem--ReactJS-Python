import React from "react";

import Header from "../../components/Header";
import Kanban from "../../components/kanban/Kanban";

import { Box } from "@mui/material";

class Users extends React.Component {

    render() {
        return(
            <Box className='outline-box'>
                <Header {...this.props} title='Usuários' subtitle='?????????????????????????' />
                <Box className='main-box'>
                    <Kanban {...this.props} />
                </Box>
            </Box>
        )
    }
}

export default Users