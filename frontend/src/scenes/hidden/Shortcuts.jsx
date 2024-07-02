import React from "react";

import Cards from "../../components/visual/Card";
import MainLabel from "../../components/inputs/MainLabel";

import { Box, Grid } from "@mui/material";
import { defaultRequest } from "../../utils/request/request";
import { imageList } from "../../utils/icons";
import { menuRelation } from "../../utils/layout";


class Shortcuts extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            favorites: [],
            lastAccess: []
        }
    }

    componentDidMount() {
        var lastAccessStorage = JSON.parse(localStorage.getItem('lastAccess'))
        var lastAccess = []

        for (var la in lastAccessStorage) {
            lastAccess.push(menuRelation[lastAccessStorage[la]])
        }

        let config = {
            method: 'get',
            endpoint: 'menu/favorite/list'
        }
        
        let form = {
            userId: this.props.user.IDUsuario
        }

        defaultRequest(config, form).then((r) => {
            if(r.status){
                this.setState({
                    favorites: r.data.favorites,
                    lastAccess: lastAccess
                })
            }
        })
    }

    redirectPage = (href) => {
        window.location.href = '#' + href
    }

    render() {
        return(
            <Box className='outline-box'>
                <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                    <MainLabel {...this.props} variant="tabSubTitle" label="Abas Favoritas" />
                    <Grid container spacing={2}>
                        {this.state.favorites.map((value) => {
                            return(
                                <Grid item md={3}><Cards {...this.props} onClick={this.redirectPage} functionProps={value.menu.url_redirect} title={value.menu.descmenu} icon={imageList[value.menu.icone]} /></Grid>
                            )
                        })}
                    </Grid>
                </Box>
                <Box mt='50px' className='main-box' backgroundColor={this.props.colors.primary[400]}>
                    <MainLabel {...this.props} variant="tabSubTitle" label="Últimos Acessos" />
                    <Grid container spacing={2}>
                        {this.state.lastAccess.map((value) => {
                            return(
                                <Grid item md={3}><Cards {...this.props} onClick={this.redirectPage} functionProps={value.to} title={value.title} icon={value.icon} /></Grid>
                            )
                        })}
                    </Grid>
                </Box>
            </Box>
        )
    }
}

export default Shortcuts