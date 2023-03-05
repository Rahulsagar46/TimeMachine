import React from "react";
import PunchRegion from "./PunchRegion";
import { DataGrid } from '@mui/x-data-grid';

const SubSection = ({ initialinfo, setInitialinfo }) => {   
    const columns = [
        { field: 'col1', headerName: 'Punch in', width: 110 },
        { field: 'col2', headerName: 'Punch out', width: 110 },
        { field: 'col3', headerName: 'Duration(hrs)', width: 110},
        { field: 'col4', headerName: 'Status', width: 110},
      ];
    
    const condition1 = initialinfo["log_entries"] !== undefined
    var condition2 = true
    if (condition1){
        var max_index = (initialinfo["log_entries"].length) - 1
        condition2 = (max_index >= 0) ? true : false 
    }
    console.log(condition1)
    console.log(condition2)
    const rows = (condition1 && condition2) ? initialinfo["log_entries"][max_index]["log_entries"].map((row) => ({
        id   : initialinfo["log_entries"][max_index]["log_entries"].indexOf(row), 
        col1 : row["log_in_time"],
        col2 : row["log_out_time"],
        col3 : row["interval_time"],
        col4 : row["log_state"]
    })) : [];  
    
    return (
        <div className="Subsection">
            <div className="Subsection1">
                <h2 className="Statusmsg">{initialinfo['live_state'] === 0 ? "You are OUT" : "You are IN"}</h2>
                <PunchRegion login_name={initialinfo['login_name']} livestate={initialinfo['live_state']} setInfo={setInitialinfo}/>
            </div>
            <div className="TodaysLog">
                { initialinfo["log_entries"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
            </div>
        </div>
    );
}

export default SubSection