import { useEffect } from "react";
import { useJobsList } from "../../hooks/useJobsList";
import "../../styles/components/list.scss"


function List() {
  const { fetchJobs, result } = useJobsList();

  useEffect(
    () => {
      fetchJobs();
    }, []
  )

  const generateTable = () => {
    if (result === null) {
      return;
    }

    return result.map((row) => (
      <tr>
        <td><a href={row.url} target="_blank">{row.job_role}</a></td>
        <td>{row.company}</td>
        <td>{row.added_at}</td>
      </tr>
    ))
  }

  return (
    <table>
      <tr className="title">
        <th>Job Role</th>
        <th>Company</th>
        <th>Added At</th>
      </tr>
      {result && generateTable()}
    </table>
  )
}

export default List;