import Link from 'next/link'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import axios from 'axios'
import React, { useState } from 'react'

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  // timeout: 60 * 30
});

const Post = () => {
  const [author, setAuthor] = useState()
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [child, setChild] = useState([])
  const [parent, setParent] = useState([])
  const [users, setUsers] = useState([])
  const [getCategories, setGetCategories] = useState([])
  React.useEffect(() => {
    const get_users = instance.get('/blogs/users').then((response) => {
      const data = response.data
      setUsers(data)
    }).catch((error) => {
      console.log(error.response)
    });
    
    const get_categories = instance.get('/blogs/categories').then((response) => {
      const data = response.data
      setGetCategories(data)
    }).catch((error) => {
      console.log(error.response)
    });
  }, []);
  async function handleOptionsChange(e) {
    let options = e.target.options;
    let value = [];
    for (let i = 0; i < options.length; i++) {
      if (options[i].selected) {
        value.push(options[i].value)
      }
    }
    // console.log(typeof e.target.id)
    if(e.target.id==='child'){
      setChild(value)
    }
    else if(e.target.id==='parent'){
      setParent(value)
    }
  }
  async function handleSubmitForm(e) {
    e.preventDefault();
    if (author && name && description && parent && child) {
      console.log(child)
      console.log(parent)
      let category = new FormData();
      category.append("author",author);
      category.append('name',name);
      category.append('description',description);
      category.append('child',child);
      category.append('parent',parent);
      console.log()
      const res = await instance.post('/blogs/categories', category, {
          // "X-CSRFToken": csrfToken,
          'Content-Type': 'application/json',
      }
      ).then((response) => {
        console.log(response.data)
      }).catch((error) => {
        console.log(error.response.data)
      });
  }
}
  return (
    <>
    <div>
      <a href="category">Add Category</a>
    </div>
    {/* {
    "author": null,
    "name": "",
    "description": "",
    "parent": [],
    "child": []
} */}
      <div>
        <form method="post" encType="multipart/form-data" onSubmit={handleSubmitForm}>
          <label htmlFor="author">author</label>
          <select onChange={(e)=>setAuthor(e.target.value)} name="user" id="cars">
          <option hidden>Select Author</option>
            {
              users.map((user) => {
                return <option key={user.username} value={user.id} >{user.username}</option>
              })
            }
          </select>
          <br />
          <label htmlFor="name">name</label>
          <input type="text" name='name' id='name' value={name} onChange={(e) => setName(e.target.value)} />
          <br />
          <label htmlFor="description">description</label>
          <input type="text" name='description ' id='description' value={description} onChange={(e) => setDescription(e.target.value)} />
          <br />
          <label htmlFor="child">child</label>
          <select name="child" id='child'
            value={child}
            onChange={
              (e) => handleOptionsChange(e)
            } multiple>
            {
              getCategories.map((category) => {
                return <option key={category.id} value={category.id} >{category.name}</option>
              })
            }
          </select>
          <br />          
          <label htmlFor="parent">parent</label>
          <select name="parent" id='parent'
            value={parent} 
            onChange={
              (e) => handleOptionsChange(e)
            } multiple>
            {
              getCategories.map((category) => {
                return <option key={category.id} value={category.id} >{category.name}</option>
              })
            }
          </select>
          <br />   
          <button type='submit'>Submit</button>
        </form>
      </div>
    </>
  )
}
export default Post 