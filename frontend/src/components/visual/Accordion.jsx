import React from "react";

import HorizontalDivider from "./HorizontalDivider";

// Icons
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

import { Accordion, AccordionDetails, AccordionSummary, Typography } from "@mui/material";


class Accordions extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            sxParams: {width: '100%', boxShadow: `3px 4px 4px ${this.props.colors.custom['boxShadow']}`, backgroundColor: this.props.colors.custom['colorWhite']}
        }
    }

    componentDidMount() {
        var css = this.state.sxParams

        css = Object.assign({}, css, this.props.customCss)

        this.setState({sxParams: css})
    }

    render() {
        return(
            <>
                <Accordion 
                    sx={this.state.sxParams} 
                    disableGutters={true}
                >
                    <AccordionSummary
                        expandIcon={<ExpandMoreIcon sx={{color: this.props.colors.grey[700]}} />}
                        aria-controls="panel1a-content"
                    >
                        <Typography color={this.props.colors.grey[500]}>{this.props.title}</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        {/* <HorizontalDivider {...this.props} /> */}
                        {this.props.content}
                    </AccordionDetails>
                </Accordion>
            </>
        )
    }
}

export default Accordions