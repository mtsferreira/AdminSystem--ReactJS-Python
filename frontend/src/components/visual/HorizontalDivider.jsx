import React from "react";

import { Divider } from "@mui/material";

class HorizontalDivider extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            sxParams: {backgroundColor: this.props.colors.grey[400]}
        }
    }

    componentWillMount() {
        var css = this.state.sxParams

        css = Object.assign({}, css, (this.props.customCss ?? {}))

        this.setState({sxParams: css})
    }

    render() {
        return(
            <Divider className="main-divider" sx={this.state.sxParams}/>
        )
    }
}

export default HorizontalDivider