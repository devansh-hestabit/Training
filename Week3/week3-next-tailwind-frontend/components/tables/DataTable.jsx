export default function DataTable() {
  const data = [
    {
      name: "Tiger Nixon",
      position: "System Architect",
      office: "Edinburgh",
      age: 61,
      startDate: "2011/04/25",
      salary: "$320,800",
    },
    {
      name: "Garrett Winters",
      position: "Accountant",
      office: "Tokyo",
      age: 63,
      startDate: "2011/07/25",
      salary: "$170,750",
    },
    {
      name: "Ashton Cox",
      position: "Junior Technical Author",
      office: "San Francisco",
      age: 66,
      startDate: "2009/01/12",
      salary: "$86,000",
    },
    {
      name: "Cedric Kelly",
      position: "Senior Javascript Developer",
      office: "Edinburgh",
      age: 22,
      startDate: "2012/03/29",
      salary: "$433,060",
    },
  ];

  return (
    <table className="w-full text-sm text-left border-collapse">
      <thead>
        <tr className="bg-gray-50 border-b">
          <th className="px-3 py-2 font-medium-semibold text-black">Name</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Position</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Office</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Age</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Start date</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Salary</th>
        </tr>
      </thead>

      <tbody>
        {data.map((row, index) => (
          <tr
            key={index}
            className={`border-b ${
              index % 2 === 0 ? "bg-white" : "bg-gray-50"
            }`}
          >
            <td className="px-3 py-2 text-gray-700">{row.name}</td>
            <td className="px-3 py-2 text-gray-700">{row.position}</td>
            <td className="px-3 py-2 text-gray-700">{row.office}</td>
            <td className="px-3 py-2 text-gray-700">{row.age}</td>
            <td className="px-3 py-2 text-gray-700">{row.startDate}</td>
            <td className="px-3 py-2 text-gray-700 ">{row.salary}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
