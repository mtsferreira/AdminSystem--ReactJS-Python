import React from 'react'

import { Card, CardContent, CardHeader, CardMedia, Typography } from '@mui/material'


class Cards extends React.Component {

    render() {
        return(
            <Card
                onClick={() => this.props.onClick(this.props.functionProps)}
                sx={{
                    backgroundColor: this.props.colors.custom['colorWhite'],
                    cursor: 'pointer',
                    ':hover': {
                        boxShadow: '20'
                    }
                }}
            >
                <CardHeader
                    avatar={this.props.icon}
                    title={<Typography>{this.props.title}</Typography>}
                />
            </Card>
        )
    }
}

export default Cards