<template>
    <section>
        <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
            v-model="name"
            :rules="nameRules"
            :counter="30"
            label="Name"
            required
            ></v-text-field>
            <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            ></v-text-field>
            <v-select
            v-model="select"
            :items="items"
            :rules="[v => !!v || 'Item is required']"
            label="Item"
            required
            ></v-select>
            <v-checkbox
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Do you agree?"
            required
            ></v-checkbox>

            <v-btn
            :disabled="!valid"
            @click="submit"
            >
            submit
            </v-btn>
            <v-btn @click="clear">clear</v-btn>
        </v-form>
        <ul>
            <li v-for="user in users">
                {{ user.name }} -- {{ user.email }}
            </li>
        </ul>
    </section>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 30) || 'Name must be less than 30 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
      ],
      checkbox: false,
      users: ''
    }),
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
          // Native form submission is not yet supported
          axios.post('http://localhost:5000/api/submit', {
            name: this.name,
            email: this.email
          })
          console.log({
            name: this.name,
            email: this.email,
            select: this.select,
            checkbox: this.checkbox
          })
        }
        this.getUsers()
      },
      clear () {
        this.$refs.form.reset()
      },
      getUsers () {
        axios.get('http://localhost:5000/api/getUsers')
          .then(res => {
            this.users = res.data
          })
      }
    },
    created () {
      this.getUsers()
    }
  }
</script>