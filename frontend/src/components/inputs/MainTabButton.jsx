import React from "react";

import { Box, Button, Typography } from "@mui/material";

class MainTabButton extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <Box
                display='flex'
                justifyContent='center'
                borderRadius='5px'
                backgroundColor={this.props.colors.custom['secondaryButton']}
                onClick={this.props.onButtonClick}
                height='100%'
                {...this.props}
            >
                <Button {...this.props} sx={{ width: '100%' }}><Typography sx={{ color: this.props.colors.custom['colorWhite'], fontWeight: '500', letterSpacing: '2px' }}>{this.props.title}</Typography></Button>
            </Box>
        )
    }
}

export default MainTabButton;