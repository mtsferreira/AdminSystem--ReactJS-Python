import React from "react";

import HorizontalDivider from "../../components/visual/HorizontalDivider";

import { Box, Typography, useTheme} from "@mui/material";
import { defaultRequest } from "../../utils/request/request";
import { imageList } from "../../utils/icons";
import { Link } from "react-router-dom";
import { menuRelation } from "../../utils/layout";
import { ProSidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { tokens } from "../../typograhpy";
import { TabsContext } from "../../TabsContext";

import "react-pro-sidebar/dist/css/styles.css";


const Item = ({title, to, icon, selected, setSelected}) => {
    const theme = useTheme()
    const colors = tokens(theme.palette.mode)
    
    return (
        <MenuItem 
            active={selected===title}              // Aba ativa
            style={{color: colors.grey[100]}}
            onClick={() => setSelected(title)}
            icon={icon}
        >
            <Typography>{title}</Typography>
            <Link to={to} />
        </MenuItem>
    )
}

class Sidebar extends React.Component {
    static contextType = TabsContext
    constructor(props){
        super(props)
        this.state = {
            hoverSidebar: this.props.isHoverSideBar,
            selected: 'Page1',
            menu: [],

            isLoaded: false
        }
    }

    componentWillMount() {
        let config = {
            method: 'get',
            endpoint: 'menu/list'
        }
        defaultRequest(config, {userId: this.props.user.IDUsuario}).then((r) => {
            if (r.status) {
                this.setState({menu: r.data.modules, isLoaded: true}, ()=>this.adjustFontSize())
            }
        })
    }

    componentDidUpdate() {
        if(this.props.activeTab && this.state.selected !== menuRelation[this.props.activeTab].title) {
            this.setState({
                selected: menuRelation[this.props.activeTab].title
            })
        }
    }
    
    adjustFontSize = () => {
        const menuItems = document.querySelectorAll('.pro-inner-item');
        
        menuItems.forEach((item, index) => {
            item.style.fontSize = '13px';  // Tamanho da fonte do menu
        });
    }

    changeActiveMenu = (title, key) => {
        this.props.switchTab(key)
        this.setState({
            selected: title,
        }, () => this.context.openTab({ key: key, title: title, content: <></> }))
    }

    render() {
        return( !this.state.isLoaded ? <></> :
            <Box
                className="sidebar-box"
                sx={{
                    '& .pro-sidebar-inner': {
                        background: `${this.props.colors.custom['bars']} !important`
                    },
                    '& .pro-icon-wrapper': {
                        backgroundColor: 'transparent !important'   
                    },
                    '& .pro-inner-item': {
                        padding: '5px 35px 5px 20px !important',
                        color: this.props.colors.custom['barsIconsAndTexts']
                    },
                    '& .pro-inner-item:hover': {
                        color: `${this.props.colors.blueAccent[500]} !important`
                    },
                    '& .pro-menu-item.active .pro-inner-item': {
                        color: `${this.props.colors.blueAccent[400]} !important`
                    },
                    '& .pro-sidebar:not(.collapsed)': {
                        width: '290px'                     // Tamanho da SideBar 
                    },
                    '& .pro-item-content p': {
                        fontSize: '13px' // Tamanho da fonte do submenu
                    }
                }}
            >
                <ProSidebar id='sidebar' collapsed={this.props.isCollapsed} onMouseEnter={this.props.handleMouseEnter} onMouseLeave={this.props.handleMouseEnter}>
                    <Menu>
                        {/* MENU ITEMS */}
                        <Box paddingLeft={this.state.isCollapsed ? undefined : '0%'}>
                            {this.state.menu?.map((value, index) => {
                                return(
                                    <>
                                        <SubMenu id={value.idmenu} key={value.idmenu} title={value.descmenu} icon={imageList[value.icone]}>
                                            {value.submenus?.map((valueS, indexS) => {
                                                return(
                                                    <Item
                                                        key={valueS.idmenu}
                                                        title={valueS.descmenu}
                                                        to={valueS.url_redirect}
                                                        selected={this.state.selected}
                                                        setSelected={(title) => this.changeActiveMenu(title, valueS.idmenu)} 
                                                    />
                                                )
                                            })}
                                        </SubMenu>
                                        <HorizontalDivider {...this.props} customCss={{margin: '0px 20px !important', backgroundColor: this.props.colors.primary[400]}} />
                                    </>
                                )
                            })}
                        </Box>
                    </Menu>
                </ProSidebar>
            </Box>
        )
    }
}

export default Sidebar