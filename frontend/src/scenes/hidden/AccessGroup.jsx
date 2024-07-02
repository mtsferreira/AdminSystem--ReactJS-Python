import React from "react";
import ReactDOM from "react-dom";

import EditableTable from "../../components/tables/EditableTable";
import Header from "../../components/Header";
import MainCheckBoxInput from "../../components/inputs/MainCheckBoxInput";
import MainLabel from "../../components/inputs/MainLabel";
import MainSelectInput from "../../components/inputs/MainSelectInput";
import MainTabButton from "../../components/inputs/MainTabButton";
import MainTextField from "../../components/inputs/MainTextField";
import SnackbarAlert from "../../components/alerts/SnackbarAlert";

// Icons
import LoadingGif from "../../components/visual/LoadingGif";

import { addLastAccess, changeActiveTabStyle } from "../../utils/layout";
import { Box, Button, Grid, Typography } from "@mui/material";
import { createEditTab } from "../../utils/layout";
import { defaultRequest, optionsRequest } from "../../utils/request/request";
import { handleChangeText } from "../../utils/handleChange";


class AccessGroup extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            isLoadingTab: true,
            isLoadingAccessGroupTable: true,
            isLoadingUserInfo: true,

            menuId: '36',

            description: '',
            status: '',
            statusOptions: [
                { 'value': 'A', 'label': 'Ativo' },
                { 'value': 'X', 'label': 'Cancelado' },
            ],

            allMenus: '',
            allUsers: '',

            userName: '',
            userList: {},

            // Lista com os ids de tela/usuario e valor FALSE para cada chave
            menuCheckboxList: {},
            userCheckboxList: {},

            // Lista com os ids das telas/usuarios que será enviado para o back
            selectedMenuList: [],
            selectedUserList: [],

            accessGroup: {},
            accessGroupList: [],
            accessGroupColumns: {},
            accessGroupTotalSize: '',

            tabs: [
                { id: 'data', title: 'Vincular Telas' },
                { id: 'users', title: 'Vincular usuários' },
            ],
        }
    }

    componentDidMount() {
        addLastAccess(this.state.menuId)
        this.onAccessGroupTableChange(0)
        optionsRequest(this, ['menu', 'userNameSurname'])
    }

    createAccessGroup = () => {
        if (!this.state.description || !this.state.status) {
            this.setState({
                alertMessage: 'Necessário preencher os campos obrigatórios (*).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'accessprofile'
        }
        let form = {
            profile: {
                descricao: this.state.description,
                situacao: this.state.status
            }
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    offersStructure: {},
                }, () => this.onAccessGroupTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    createEditTab = (params) => {
        this.setState({
            selectedRow: params,
            isLoadingTab: true,
            activeTab: 'data',
        }, () => createEditTab('Grupo', this.state.tabs, this.props, this.handleChangeTab, this.onCloseEditTab))
    }

    deleteAccessGroup = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'accessprofile/search'
        }
        let form = {
            id: id
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.onAccessGroupTableChange(0))
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    deleteMenu = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
            relationId: id,
            type: 'menu',
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.searchAccessGroupInfo())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    deleteUser = (id) => {
        let config = {
            method: 'delete',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
            relationId: id,
            type: 'user',
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.searchAccessGroupInfo())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    handleChangeTab = (event) => {
        if (this.state.isLoadingTab) {
            ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchAccessGroupInfo(0))
            return
        }
        if (!this.state.accessGroup) {
            return
        }
        var page = event?.target.id ? event?.target.id : this.state.activeTab ?? this.state.tabs[0]['id']

        changeActiveTabStyle(this.state.tabs, page, this.props.colors)

        var context = ''
        if (page === 'data') {
            context =
                <Box sx={{ flexGrow: 1 }}>
                    <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '15px 0' }}>
                        <Grid item md={12} sx={{ width: '100%' }}>
                            <Box
                                width='99%'
                                border='1px solid'
                                borderRadius='5px'
                                padding='0 10px 10px 5px'
                                marginBottom='15px'
                                borderColor={this.props.colors.grey[1100]}
                                boxShadow={`3px 3px 3px ${this.props.colors.custom['boxShadow']}`}
                            >
                                <Grid container columnSpacing={1} rowSpacing={2} sx={{ flexDirection: { xs: 'column', sm: 'column', md: 'row' }, margin: '10px 0' }}>
                                    <Grid item md={8}><MainTextField required {...this.props} id='descricao' value={this.state.accessGroup.descricao} label='Descrição' handleChange={this.handleChangeTextTab} width={{ xs: '97%', md: '97%', lg: '100%' }} /></Grid>
                                    <Grid item md={2}><MainSelectInput required {...this.props} id='situacao' value={this.state.accessGroup.situacao} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeTextTab} width={{ xs: '97%', md: '97%', lg: '100%' }} /></Grid>

                                    <Grid item md={2}>
                                        <MainTabButton sx={{ width: { xs: '97%', sm: '97%', md: '95%' } }} {...this.props} onButtonClick={this.updateAccessGroup} title="Salvar" />
                                    </Grid>
                                </Grid>
                            </Box>
                        </Grid>

                        {/* Incluir menus */}
                        <Grid item md={12}>
                            <Box
                                sx={{
                                    width: '99%',
                                    border: '2px solid',
                                    borderRadius: '5px',
                                    borderColor: this.props.colors.grey[1100],
                                    boxShadow: `3px 3px 3px ${this.props.colors.custom['boxShadow']}`,

                                }}
                            >
                                <Box
                                    sx={{
                                        display: 'flex',
                                        flexDirection: { xs: 'column', sm: 'column', md: 'row' },
                                        alignItems: 'center',
                                        justifyContent: 'space-between',

                                        borderBottom: `1px solid ${this.props.colors.grey[1100]}`,
                                        padding: '0 15px'
                                    }}
                                >
                                    <Button sx={{ background: this.props.colors.custom['secondaryButton'], color: 'white', letterSpacing: '1px', height: '70%', width: { xs: '97%', sm: '97%', md: '10%' }, margin: '10px 0' }} {...this.props} variant='contained' onClick={this.saveAccessPages}>Salvar</Button>

                                    <Typography sx={{ fontWeight: 'bold', fontSize: '14px' }}>Telas de Acesso:</Typography>

                                    <Button sx={{ background: 'transparent', height: '70%', width: { xs: '97%', sm: '97%', md: '15%' }, margin: '10px 0', color: 'black', ":hover": { background: this.props.colors.grey[800] } }} {...this.props} variant='contained' onClick={() => this.selectAllCheckbox('menuCheckboxList', 'selectedMenuList')}>Selecionar todos</Button>
                                </Box>

                                <Box
                                    sx={{
                                        mr: '45px',
                                        display: 'grid',
                                        gap: '15px',
                                        gridTemplateColumns: {
                                            xs: '50% 50%',
                                            md: '50% 50%',
                                            lg: '20% 20% 20% 20% 20%',
                                        },
                                        padding: '15px 15px'
                                    }}
                                >
                                    {this.state.menuOptions.map((item) => {
                                        return (
                                            <MainCheckBoxInput sx={{ '& .MuiFormControlLabel-label': { fontSize: '14px' }, '& .MuiFormControlLabel-root': { padding: '14px' } }} {...this.props} id='idmenu' value={this.state.menuCheckboxList[item.idmenu]} label={item.label} handleChange={(event) => this.handleChangeCheckboxTabMenu(event, item.idmenu)} />
                                        )
                                    })}
                                </Box>

                            </Box>
                        </Grid>
                    </Grid>
                </Box >

        } else if (page === 'users') {
            if (this.state.isLoadingUserInfo) {
                ReactDOM.render(<LoadingGif />, document.getElementById('inside-edit-box'), () => this.searchUsersByName())
                return
            }
            context =
                <>
                    <Box sx={{ flexGrow: 1 }}>

                        <Box
                            sx={{
                                width: '98.5%',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '80% 20%',
                                },
                                marginTop: '15px'
                            }}
                        >
                            <MainTextField {...this.props} id='userName' value={this.state.userName || ''} label='Nome do usuário' handleChange={this.handleChangeTextTabUser} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'], height: '100%', width: { xs: '100%', md: '100%', lg: '95%' } }} {...this.props} variant='contained' onClick={this.searchUsersByName}>Buscar</Button>
                        </Box>

                        {/* Incluir usuários */}
                        <Box
                            sx={{
                                width: '99%',
                                border: '2px solid',
                                borderRadius: '5px',
                                borderColor: this.props.colors.grey[1100],
                                boxShadow: `3px 3px 3px ${this.props.colors.custom['boxShadow']}`,
                                marginTop: '20px',
                                maxHeight: '70vh',
                                overflowY: 'auto'
                            }}
                        >
                            <Box
                                sx={{
                                    display: 'flex',
                                    flexDirection: { xs: 'column', sm: 'column', md: 'row' },
                                    alignItems: 'center',
                                    justifyContent: 'space-between',

                                    borderBottom: `1px solid ${this.props.colors.grey[1100]}`,
                                    padding: '0 15px',

                                }}
                            >
                                <Button sx={{ background: this.props.colors.custom['secondaryButton'], color: 'white', letterSpacing: '1px', height: '70%', width: { xs: '97%', sm: '97%', md: '10%' }, margin: '10px 0' }} {...this.props} variant='contained' onClick={this.saveAccessUsers}>Salvar</Button>

                                <Typography sx={{ fontWeight: 'bold', fontSize: '14px' }}>Usuários com Acesso:</Typography>

                                <Button sx={{ background: 'transparent', height: '70%', width: { xs: '97%', sm: '97%', md: '15%' }, margin: '10px 0', color: 'black', ":hover": { background: this.props.colors.grey[800] } }} {...this.props} variant='contained' onClick={() => this.selectAllCheckbox('userCheckboxList', 'selectedUserList')}>Selecionar todos</Button>
                            </Box>

                            <Box
                                sx={{
                                    mr: '45px',
                                    display: 'grid',
                                    gap: '15px',
                                    gridTemplateColumns: {
                                        xs: '50% 50%',
                                        md: '50% 50%',
                                        lg: '20% 20% 20% 20% 20%',
                                    },
                                    padding: '15px 15px'
                                }}
                            >
                                {this.state.userList.map((item) => {
                                    return (
                                        <MainCheckBoxInput sx={{ '& .MuiFormControlLabel-label': { fontSize: '12px' }, '& .MuiFormControlLabel-root': { padding: '14px' } }} {...this.props} id='idusuario' value={this.state.userCheckboxList[item.idusuario]} label={item.label} handleChange={(event) => this.handleChangeCheckboxTabUser(event, item.idusuario)} />
                                    )
                                })}

                            </Box>
                        </Box>

                    </Box>
                </>
        }
        ReactDOM.render(context, document.getElementById('inside-edit-box'), () => this.setState({ activeTab: page }))
    }

    handleChangeText = (event) => {
        this.setState({ [event.target.id]: event.target.value })
    }

    handleChangeTextTab = (event) => {
        handleChangeText(this.state.accessGroup, event.target.id, event.target.value, () => this.handleChangeTab())
    }

    handleChangeCheckboxTabMenu = (event, idmenu) => {
        const isCurrentlySelected = this.state.menuCheckboxList[idmenu];

        this.setState((prevState) => ({
            menuCheckboxList: { ...prevState.menuCheckboxList, [idmenu]: !isCurrentlySelected }
        }));

        if (!isCurrentlySelected) {
            this.setState(prevState => ({
                selectedMenuList: [...prevState.selectedMenuList, idmenu]
            }), () => this.handleChangeTab());
        } else {
            this.setState(prevState => ({
                selectedMenuList: prevState.selectedMenuList.filter(item => item !== idmenu),
            }), () => this.handleChangeTab());
        }
    }

    handleChangeCheckboxTabUser = (event, idusuario) => {
        const isCurrentlySelected = this.state.userCheckboxList[idusuario];

        this.setState((prevState) => ({
            userCheckboxList: { ...prevState.userCheckboxList, [idusuario]: !isCurrentlySelected }
        }));

        if (!isCurrentlySelected) {
            this.setState(prevState => ({
                selectedUserList: [...prevState.selectedUserList, idusuario]
            }), () => this.handleChangeTab());
        } else {
            this.setState(prevState => ({
                selectedUserList: prevState.selectedUserList.filter(item => item !== idusuario),
            }), () => this.handleChangeTab());
        }
    }

    handleChangeTextTabUser = (event) => {
        this.setState({ [event.target.id]: event.target.value }, () => this.handleChangeTab())
    }

    onAccessGroupTableChange = (page) => {
        let config = {
            method: 'get',
            endpoint: 'accessprofile/search'
        }
        let form = {
            page: page,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    accessGroupList: r.data.access_group,
                    accessGroupColumns: r.data.columns,
                    accessGroupTotalSize: r.data.total_size,

                    isLoading: false,
                    isLoadingAccessGroupTable: false
                })
            }
        })
    }

    onAccessGroupTableEdit = (row, method, extraParam) => {
        if (method === 'delete') {
            this.setState({
                accessGroupList: row
            }, () => this.deleteAccessGroup(extraParam))
        }
    }

    onCloseEditTab = () => {
        this.setState({
            isLoadingTab: true,
            isLoadingUserInfo: true,
            selectedMenuList: [],
            selectedUserList: [],
            menuCheckboxList: {},
            userCheckboxList: {},
            accessGroup: {},
            userName: '',
            selectedRow: '',
        }, () => this.onAccessGroupTableChange(0))
    }

    populateMenuCheckboxList = () => {
        const newMenuCheckboxList = {};
        this.state.menuOptions.forEach(option => {
            newMenuCheckboxList[option.value] = false;
        })

        this.setState({ menuCheckboxList: newMenuCheckboxList }, () => this.updateActiveMenus())
    }

    populateUserCheckboxList = () => {
        const newUserCheckboxList = {};
        this.state.userList.forEach(option => {
            newUserCheckboxList[option.value] = false;
        })

        this.setState({ userCheckboxList: newUserCheckboxList }, () => this.updateActiveUsers())
    }

    saveAccessPages = () => {
        let config = {
            method: 'post',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
            profile: {
                menus: this.state.selectedMenuList,
            },
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isLoadingTab: true,
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    saveAccessUsers = () => {
        let config = {
            method: 'post',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
            profile: {
                users: this.state.selectedUserList,
            },
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,

                    isLoadingTab: true,
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    searchAccessGroupInfo = () => {
        let config = {
            method: 'get',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {

                this.setState({
                    accessGroup: r.data.profile,

                    isLoadingTab: false,
                }, () => this.populateMenuCheckboxList())
            }
        })
    }

    searchUsersByName = () => {
        let config = {
            method: 'get',
            endpoint: 'user/search'
        }
        let form = {
            term: this.state.userName,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    userList: r.data.userList,

                    activeTab: 'users',
                    isLoadingUserInfo: false,
                }, () => this.populateUserCheckboxList())
            }
        })
    }

    selectAllCheckbox = (checkboxList, selectedList) => {
        const currentCheckboxList = this.state[checkboxList];

        const allTrue = Object.keys(currentCheckboxList).every(key => currentCheckboxList[key]);

        const updatedCheckboxList = {};
        Object.keys(currentCheckboxList).forEach(key => {
            updatedCheckboxList[key] = !allTrue;
        });

        const selectedIds = Object.keys(updatedCheckboxList).filter(key => updatedCheckboxList[key] === true);

        this.setState({ [checkboxList]: updatedCheckboxList, [selectedList]: selectedIds }, () => this.handleChangeTab());
    }

    updateAccessGroup = () => {
        if (!this.state.accessGroup.descricao || !this.state.accessGroup.situacao) {
            this.setState({
                alertMessage: 'Necessário preencher os campos obrigatórios (*).',
                alertType: 'error',
                showAlert: true
            })
            return
        }
        let config = {
            method: 'post',
            endpoint: 'accessprofile'
        }
        let form = {
            id: this.state.selectedRow.idperfil,
            profile: this.state.accessGroup,
        }
        defaultRequest(config, form).then((r) => {
            if (r.status) {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'success',
                    showAlert: true,
                }, () => this.handleChangeTab())
            } else {
                this.setState({
                    alertMessage: r.data.message,
                    alertType: 'error',
                    showAlert: true
                })
            }
        })
    }

    updateActiveMenus = () => {
        if (this.state.accessGroup.menu_list.length !== 0) {

            const updatedSelectedMenus = new Set(this.state.selectedMenuList);

            this.state.accessGroup.menu_list.forEach(item => {
                if (item.idmenu in this.state.menuCheckboxList) {
                    this.setState(prevState => ({
                        // Compara as duas listas e muda para true em 'menuCheckboxList' os ids que estiverem em ambas
                        menuCheckboxList: {
                            ...prevState.menuCheckboxList,
                            [item.idmenu]: true
                        }
                    }));
                    // Adiciona somente os ids, que estão como TRUE, em uma lista
                    updatedSelectedMenus.add(item.idmenu);
                }
            });
            // Seta os ids dentro do estado selectedMenuList
            this.setState({ selectedMenuList: Array.from(updatedSelectedMenus) }, () => this.handleChangeTab())
        } else {
            this.handleChangeTab();
        }
    }

    updateActiveUsers = () => {
        if (this.state.accessGroup.usuarios.length !== 0) {

            const updatedSelectedUsers = new Set(this.state.selectedUserList);

            this.state.accessGroup.usuarios.forEach(item => {
                if (item.idusuario in this.state.userCheckboxList) {
                    this.setState(prevState => ({
                        // Compara as duas listas e muda para true em 'userCheckboxList' os ids que estiverem em ambas
                        userCheckboxList: {
                            ...prevState.userCheckboxList,
                            [item.idusuario]: true
                        }
                    }));
                    // Adiciona somente os ids, que estão como TRUE, em uma lista
                    updatedSelectedUsers.add(item.idusuario);
                }
            });
            // Seta os ids dentro do estado selectedUserList
            this.setState({ selectedUserList: Array.from(updatedSelectedUsers) }, () => this.handleChangeTab())
        } else {
            this.handleChangeTab();
        }
    }


    render() {
        if (this.state.isLoading) {
            return (
                <></>
            )
        }
        return (
            <>
                {this.state.showAlert ? <SnackbarAlert alertType={this.state.alertType} open={true} message={this.state.alertMessage} onClose={() => this.setState({ showAlert: false, alertMessage: '' })} /> : <></>}
                <Box className='outline-box'>
                    <Header {...this.props} title='Grupos de Acesso' menuId={this.state.menuId} showFav />
                    <Box className='main-box' backgroundColor={this.props.colors.primary[400]}>
                        <MainLabel {...this.props} variant="tabSubTitle" label="Criar Grupo" />
                        <Box
                            sx={{
                                mr: '45px',
                                display: 'grid',
                                gap: '15px',
                                gridTemplateColumns: {
                                    md: '100%',
                                    lg: '55% 15% 15% 15%',
                                },
                            }}
                        >
                            <MainTextField required {...this.props} id='description' value={this.state.description} label='Descrição' handleChange={this.handleChangeText} width='100%' />
                            <MainSelectInput required {...this.props} id='status' value={this.state.status} optionsList={this.state.statusOptions} label='Situação' handleChange={this.handleChangeText} width='100%' />

                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' width='97%' onClick={this.createAccessGroup}>Inserir</Button>
                            <Button sx={{ background: this.props.colors.custom['searchButtons'] }} {...this.props} variant='contained' width='97%' onClick={() => this.setState({ description: '', status: '' })}>Limpar</Button>
                        </Box>

                        <EditableTable
                            {...this.props}
                            id='idperfil'
                            allowEdit
                            noDeleteButton
                            data={this.state.accessGroupList}
                            columns={this.state.accessGroupColumns}
                            rowId='idperfil'
                            totalSize={this.state.accessGroupTotalSize}
                            onPageChange={this.onAccessGroupTableChange}
                            onEditRow={this.onAccessGroupTableEdit}
                            onRowDoubleClick={(params) => this.createEditTab(params, false)}
                            isLoading={this.state.isLoadingAccessGroupTable}
                            extraColumnsConfig={
                                {
                                    'situacao': {
                                        'type': 'select',
                                        'options': this.state.statusOptions
                                    }
                                }
                            }
                        />
                    </Box>
                </Box>
            </>
        )
    }
}

export default AccessGroup;