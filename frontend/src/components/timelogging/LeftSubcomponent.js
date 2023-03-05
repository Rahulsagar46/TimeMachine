import React from 'react';
import { DataGrid } from '@mui/x-data-grid';

const LeftSubcomponent = ({ initialinfo, setInitialinfo }) => {
    const columns = [
        { field: 'col1', headerName: 'Date', width: 110 },
        { field: 'col2', headerName: 'Day', width: 110 },
        { field: 'col3', headerName: 'Total Working time', width: 130 },
        { field: 'col4', headerName: 'Net Working time', width: 130}
      ];
      console.log(initialinfo["log_entries"])
      const rows = initialinfo["log_entries"] === undefined ? [] : initialinfo["log_entries"].map((row) => ({
          id   : initialinfo["log_entries"].indexOf(row), 
          col1 : row["date"],
          col2 : row["week_day"],
          col3 : row["total_work_time_for_day"],
          col4 : '-00:30'
      }));
      
    return (
        <div className='LeftSubcomponent'>
            { initialinfo["log_entries"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
        </div>
    );
}

export default LeftSubcomponent