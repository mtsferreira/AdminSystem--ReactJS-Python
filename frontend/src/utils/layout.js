import ReactDOM from "react-dom";

import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import Header from "../components/Header";
import HorizontalDivider from "../components/visual/HorizontalDivider";

import { Box, Button, IconButton } from "@mui/material";
import { imageList } from "./icons";

export function changeActiveTabStyle(tabs, page, colors) {
    for (let tab in tabs) {
        let el = document.getElementById(tabs[tab]['id'])
        el.style.backgroundColor = tabs[tab]['id'] === page ? `${colors.grey[600]}` : 'transparent'
        el.style.borderRadius = tabs[tab]['id'] === page ? '3px' : '0'
        el.style.height = '30px'
        el.style.fontSize = '12px'
        el.style.marginRight = '12px'
        el.style.paddingTop = '10px'
        el.style.color = tabs[tab]['id'] === page ? `${colors.custom['colorWhite']}` : `${colors.primary[100]}`
        el.style.borderBottom = tabs[tab]['id'] === page ? '0.5px solid transparent' : `1px solid ${colors.grey[600]}`
    }
}

export function createEditTab(title, tabList, props, callback, closeCallback) {
    var body =
        <Box id='edit-box' borderRadius='0 0 25px 25px' backgroundColor={props.colors.custom['colorWhite']} padding='20px' sx={{ contain: 'content', width: { xs: '100vw', sm: '100vw', md: '75vw' }, position: { md: 'absolute' }, transform: { md: 'translate(-15%, 0)' } }}>
            <Box
                display='flex'
                justifyContent='space-between'
                alignItems='center'
                sx={{
                    '& .MuiButtonBase-root': {
                        color: props.colors.grey[100]
                    }
                }}
            >
                <Header {...props} variant='h5' color={props.colors.grey[100]} title={title} />
                <IconButton sx={{ marginTop: '-15px' }}><CloseOutlinedIcon onClick={() => {
                    document.getElementById('edit-tab').remove()
                    closeCallback()
                }} /></IconButton>
            </Box>
            <Box
                sx={{
                    '& .MuiButtonBase-root': {
                        color: props.colors.grey[100]
                    },
                    flexGrow: 1
                }}
            >
                <Box id='scroll-filter'
                    sx={{
                        '&::-webkit-scrollbar-thumb': {
                            backgroundColor: props.colors.blueAccent[500],
                            borderRadius: '10px',
                        },
                        '&::-webkit-scrollbar-track': {
                            background: props.colors.custom['colorWhite']
                        },
                        '&::-webkit-scrollbar': {
                            height: '7px'
                        },
                    }}
                >
                    {tabList.map((value) => {
                        return (
                            <Button className="tab-button" onClick={callback} id={value['id']} style={{ marginRight: '5px', letterSpacing: '2px', fontWeight: '600', marginBottom: '5px' }}>{value['title'].toUpperCase()}</Button>
                        )
                    })}
                </Box>
            </Box>
            <HorizontalDivider {...props} customCss={{ margin: '0 !important' }} />
            <Box id='inside-edit-box'>
            </Box>
        </Box>

    const app = document.getElementById('app')
    const element = document.createElement('div')
    element.id = 'edit-tab'
    element.style.zIndex = '10'
    element.style.width = '100vw'
    element.style.height = '100vh'
    element.style.backgroundColor = '#00000080'
    element.style.position = 'fixed'
    element.style.overflowX = 'hidden'

    app.appendChild(element)
    ReactDOM.render(body, element, (event) => callback(event))
}

export const menuRelation = {
    '2': { title: 'Gráfico Dashboard', icon: imageList['LeaderboardOutlined'], to: '/graphics' },
    '4': { title: 'Clientes', icon: imageList['PersonOutlineOutlined'], to: '/customers' },
    '5': { title: 'Representadas', icon: imageList['PersonOutlineOutlined'], to: '/represented' },
    '7': { title: 'Cadastro Produto', icon: imageList['BlenderOutlined'], to: '/productregister' },
    '9': { title: 'Tabelas de Preços', icon: imageList['LocalAtmOutlined'], to: '/prices' },
    '11': { title: 'WorkFlow de Orçamentos', icon: imageList['GradingOutlined'] },
    '12': { title: 'Carteira de Pedido', icon: imageList['GradingOutlined'], to: '/orderbook' },
    '14': { title: 'Empresa Controladora', icon: imageList['StorefrontOutlined'], to: '/company' },
    '15': { title: 'Locais de Venda', icon: imageList['StorefrontOutlined'], to: '/localsale' },
    '17': { title: 'Ofertas', icon: imageList['BusinessCenterOutlined'], to: '/offers' },
    '18': { title: 'Políticas de Comissões', icon: imageList['BusinessCenterOutlined'], to: '/commissionpolicies' },
    '19': { title: 'Comissões x Desconto', icon: imageList['BusinessCenterOutlined'], to: '/commissiondiscount' },
    '20': { title: 'Preço x Estrutura', icon: imageList['BusinessCenterOutlined'], to: '/pricestructure' },
    '21': { title: 'Preço x Prazo', icon: imageList['BusinessCenterOutlined'] },
    '22': { title: 'Desconto Volume', icon: imageList['BusinessCenterOutlined'], to: '/volumediscount' },
    '23': { title: 'Desconto por Tipo Cliente', icon: imageList['BusinessCenterOutlined'], to: '/customertypediscount' },
    '24': { title: 'Frete CIF', icon: imageList['BusinessCenterOutlined'], to: '/shippingcif' },
    '38': { title: 'Tipo de Pedido', icon: imageList['TuneOutlined'], to: '/ordertype' },
    '26': { title: 'Condições de Pagamento', icon: imageList['TuneOutlined'], to: '/payment' },
    '27': { title: 'Prazo de Pagamento', icon: imageList['TuneOutlined'], to: '/paymentterm' },
    '28': { title: 'Desconto Comercial', icon: imageList['TuneOutlined'], to: '/comercialdiscount' },
    '29': { title: 'Linhas de Produto', icon: imageList['TuneOutlined'], to: '/productlines' },
    '30': { title: 'Margens', icon: imageList['TuneOutlined'], to: '/margins' },
    '31': { title: 'Regras de Preços', icon: imageList['TuneOutlined'], to: '/pricerules' },
    '32': { title: 'Mensagens', icon: imageList['TuneOutlined'], to: '/portalmessage' },
    '33': { title: 'Regiões de Vendas', icon: imageList['TuneOutlined'], to: '/salesregion' },
    '34': { title: 'WorkFlow', icon: imageList['TuneOutlined'], to: '/workflow' },
    '36': { title: 'Perfil de Acesso', icon: imageList['AccountCircleOutlined'], to: '/accessgroup' },
    '37': { title: 'Usuários', icon: imageList['AccountCircleOutlined'] },
}

export function addLastAccess(menuId) {
    var lastAccessStorage = JSON.parse(localStorage.getItem('lastAccess') || '[]')

    if (lastAccessStorage.includes(menuId)) {
        lastAccessStorage.splice(lastAccessStorage.indexOf(menuId), 1)
    }
    lastAccessStorage.unshift(menuId)

    if (lastAccessStorage.length > 8) {
        lastAccessStorage = lastAccessStorage.slice(0, 8)
    }

    localStorage.setItem('lastAccess', JSON.stringify(lastAccessStorage))
}

export function showUnauthorizedModal() {
    // Cria o fundo do modal
    const modalBackground = document.createElement('div')
    modalBackground.style.position = 'fixed'
    modalBackground.style.top = '0'
    modalBackground.style.left = '0'
    modalBackground.style.width = '100%'
    modalBackground.style.height = '100%'
    modalBackground.style.backgroundColor = 'rgba(0, 0, 0, 0.5)'
    modalBackground.style.zIndex = '1000'

    // Cria o conteúdo do modal
    const modalBody = document.createElement('div')
    modalBody.style.position = 'fixed'
    modalBody.style.top = '50%'
    modalBody.style.left = '50%'
    modalBody.style.transform = 'translate(-50%, -50%)'
    modalBody.style.backgroundColor = '#FFF'
    modalBody.style.borderRadius = '10px'
    modalBody.style.padding = '20px'
    modalBody.style.zIndex = '1001'

    const boldText = document.createElement('strong')
    boldText.textContent = 'Sessão Expirada'
    boldText.fontSize = '28px'
    boldText.style.display = 'block'
    boldText.style.marginBottom = '10px'

    const normalText = document.createElement('span')
    normalText.textContent = 'Sua sessão expirou. Faça login novamente.'

    // Criar o elemento parágrafo e adicionar os dois elementos de texto a ele
    const modalText = document.createElement('p')
    modalText.appendChild(boldText)
    modalText.appendChild(document.createElement('br'))
    modalText.appendChild(normalText)

    modalBody.appendChild(modalText)

    // Adiciona o botão de redirecionamento
    const button = document.createElement('button')
    button.textContent = 'LOGIN'
    button.style.color = '#6870fa'
    button.style.backgroundColor = 'transparent'
    button.style.textDecoration = 'none'
    button.style.fontWeight = 'bold'
    button.style.display = 'block' 
    button.style.marginLeft = 'auto' 
    button.style.marginTop = '25px' 
    button.style.border = 'none' 
    button.style.cursor = 'pointer'
    button.onclick = function () {
        window.location.href = '/#/login'
        window.location.reload()
    }
    modalBody.appendChild(button)

    // Adiciona o modal ao body
    document.body.appendChild(modalBackground)
    document.body.appendChild(modalBody)
}