import React from "react";

import HorizontalDivider from "../visual/HorizontalDivider";

import { Typography } from "@mui/material";


class MainLabel extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            sxParams: {}
        }
    }

    componentWillMount() {
        var css = {}
        if (this.props.variant === 'tabTitle') {
            css = {
                fontSize: '18px',
                letterSpacing: '2px',
            }
        } else if (this.props.variant === 'tabInput') {
            css = {
                fontSize: '14px',
                letterSpacing: '2px',
                // textAlign: 'right'
            }
        } else if (this.props.variant === 'tabSubTitle') {
            css = {
                fontSize: '16px',
                letterSpacing: '1px',
                marginTop: '3px',
            }
        } else if (this.props.variant === 'tabSubSubTitle') {
            css = {
                fontSize: '14px',
                letterSpacing: '1px',
                marginTop: '5px',
            }
        }

        this.setState({
            sxParams: Object.assign({}, css, this.state.sxParams)
        })
    }

    render() {
        return (
            <>
                <Typography
                    sx={{
                        color: this.props.colors.grey[200],
                        ...this.state.sxParams
                    }}
                >{this.props.label}</Typography>
                {this.props.variant === 'tabTitle' ? <HorizontalDivider {...this.props} customCss={{ margin: '5px 0 30px 0 !important' }} /> : <></>}
                {this.props.variant === 'tabSubTitle' ? <HorizontalDivider {...this.props} customCss={{ margin: '5px 10px 20px 0 !important', width: '100%' }} /> : <></>}
                {this.props.variant === 'tabSubSubTitle' ? <HorizontalDivider {...this.props} customCss={{ margin: '5px 50px 10px 0 !important', width: '100%' }} /> : <></>}
            </>
        )
    }
}

export default MainLabel