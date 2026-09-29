function load_jobs(current_search=null, current_status=null){
            error_display.textContent=""
            container.innerHTML="Loading jobs..."
            let url
            if (current_search===null && current_status===null){
                url="/jobs"
            }
            else if(current_status===null){
                url=`/jobs?search=${current_search}`
            }
            else if(current_search===null){
                url=`/jobs?status=${current_status}`
            }
            else{
                url=`/jobs?search=${current_search}&status=${current_status}`
            }
            fetch(url)
            .then(function(response) {
                if(!response.ok){
                    return response.json()
                    .then(function(data){
                        throw new Error(`Error: ${data["error"]}`)
                    })
                }
                return response.json()
            })    
            .then(function(data){
                container.innerHTML=""
                if(data.length === 0){
                    if(current_search===null && current_status===null){
                        container.textContent="No Jobs yet!"
                        return
                    }
                    else{
                        container.textContent="No matching results!"
                        return
                    }
                }
                for(let job of data){
                   let jobDiv=document.createElement("div")
                   let id_p=document.createElement("p")
                   let company_p=document.createElement("p")
                   let role_p=document.createElement("p")
                   let status_p=document.createElement("p")
                   let location_p=document.createElement("p")
                   let salary_p=document.createElement("p")
                   let delete_b=document.createElement("button")
                   let edit_b=document.createElement("button")
                   let seporator=document.createElement("div")
                   seporator.textContent="==================="
                   let spacee=document.createElement("br")
                   id_p.textContent=`ID: ${job["id"]}`
                   company_p.textContent=`Compnay: ${job["company"]}`
                   role_p.textContent=`Role: ${job["role"]}`
                   status_p.textContent=`Status: ${job["status"]}`
                   location_p.textContent=`location: ${job["location"]}`
                   salary_p.textContent=`Salary: ${job["salary"]}`
                    delete_b.textContent="DELETE"
                    delete_b.onclick=function(){delete_job(job["id"])}
                    edit_b.textContent="EDIT"
                    edit_b.onclick= function(){edit_job(job["id"])}
                    jobDiv.appendChild(id_p)
                    jobDiv.appendChild(company_p)
                    jobDiv.appendChild(role_p)
                    jobDiv.appendChild(status_p)
                    jobDiv.appendChild(location_p)
                    jobDiv.appendChild(salary_p)
                    jobDiv.appendChild(delete_b)
                    jobDiv.appendChild(edit_b)
                    jobDiv.appendChild(seporator)
                    jobDiv.appendChild(spacee)
                    container.appendChild(jobDiv)
                }     

            })
            .catch(function(error){
                container.innerHTML=""
                error_display.textContent=error.message
            })
        }