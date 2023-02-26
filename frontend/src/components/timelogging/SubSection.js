import React from "react";
import PunchRegion from "./PunchRegion";
import { DataGrid } from '@mui/x-data-grid';

const SubSection = ({ initialinfo, setInitialinfo }) => {   
    const columns = [
        { field: 'col1', headerName: 'Punch in', width: 120 },
        { field: 'col2', headerName: 'Punch out', width: 120 },
        { field: 'col3', headerName: 'Duration(hrs)', width: 120},
        { field: 'col4', headerName: 'Status', width: 120},
      ];

      const rows = [
        { id: 1, col1: '12:50:01', col2: '13:50:01', col3:'1', col4: 'settled'},
        { id: 2, col1: '14:20:01', col2: '14:50:01', col3:'0.5', col4: 'settled'},
        { id: 3, col1: '15:10:08', col2: '15:30:10', col3:'0.25', col4:'settled' },
        { id: 4, col1: '16:10:08', col2: '', col3:'', col4:'unsettled' }
      ];
    
    return (
        <div className="Subsection">
            <div className="Subsection1">
                <h2 className="Statusmsg">{initialinfo['live_state'] === 0 ? "You are OUT" : "You are IN"}</h2>
                <PunchRegion login_name={initialinfo['login_name']} livestate={initialinfo['live_state']} setInfo={setInitialinfo}/>
                {/* <div className="TodaysLog"></div> */}
            </div>
            <div className="TodaysLog">
                    <DataGrid rows={rows} columns={columns} rowHeight={30} />
            </div>
        </div>
    );
}

export default SubSection