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
  // {
  //     "post": null,
  //     "author": null,
  //     "description": ""
  // }
  const [author, setAuthor] = useState()
  const [post, setPost] = useState("")
  const [description, setDescription] = useState("")
  const [users, setUsers] = useState([])
  const [posts, setPosts] = useState([])

  React.useEffect(() => {
    const get_users = instance.get('/blogs/users').then((response) => {
      const data = response.data
      setUsers(data)
    }).catch((error) => {
      console.log(error.response)
    });
    const get_posts = instance.get('/blogs/posts').then((response) => {
      const data = response.data
      setPosts(data)
    }).catch((error) => {
      console.log(error.response)
    });
  }, []);
  async function handleSubmitForm(e) {
    e.preventDefault();
    if (author && post && description) {
      let comment = new FormData();
      comment.append("author", author);
      comment.append('post', post);
      comment.append('description', description);
      const res = await instance.post('/blogs/comments', comment, {
        // "X-CSRFToken": csrfToken,
        'Content-Type': 'application/json',
      }).then((response) => {
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
          <select onChange={(e) => setAuthor(e.target.value)} name="user" id="cars">
            <option hidden>Select Author</option>
            {
              users.map((user) => {
                return <option key={user.username} value={user.id} >{user.username}</option>
              })
            }
          </select>
          <br />
          <label htmlFor="post">post</label>
          <select onChange={(e) => setPost(e.target.value)} name="user" id="cars">
            <option hidden>Select Post</option>
            {
              posts.map((post) => {
                return <option key={post.id} value={post.id} >{post.summary}</option>
              })
            }
          </select>
          <label htmlFor="description">description</label>
          <input type="text" name='description ' id='description' value={description} onChange={(e) => setDescription(e.target.value)} />
          <br />
          <button type='submit'>Submit</button>
        </form>
      </div>
    </>
  )
}
export default Post 