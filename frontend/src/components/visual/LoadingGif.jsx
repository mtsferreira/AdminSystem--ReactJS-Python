import React from "react";

class LoadingGif extends React.Component {

    render() {
        return ( 
            <div style={{
                margin: 'auto',
                width: '100%',
                height: '100%',
                backgroundColor: '#00000000',
                zIndex: '100',
                textAlign: 'center',
                marginTop: '150px',
                marginBottom: '150px'

            }} >
                <img style={{

                    width: '100px',
                    height: '100px',
                    margin: 'auto',
                }} src="https://www.superiorlawncareusa.com/wp-content/uploads/2020/05/loading-gif-png-5.gif" alt="Carregando..." />
            </div>
        )
    }
}

export default LoadingGif