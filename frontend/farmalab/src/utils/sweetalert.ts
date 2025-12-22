import Swal from 'sweetalert2'

export const Toast = Swal.mixin({
  position: 'center',
  showConfirmButton: true,
  showCancelButton: false,
  customClass: {
    popup: 'rounded-2xl',
    confirmButton: 'bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 px-6 rounded-lg',
    cancelButton: 'bg-gray-300 hover:bg-gray-400 text-gray-700 font-semibold py-2 px-6 rounded-lg'
  },
  buttonsStyling: false
})

export const confirmAlert = (options: {
  title: string
  text?: string
  confirmButtonText?: string
  cancelButtonText?: string
}) => {
  return Swal.fire({
    title: options.title,
    text: options.text,
    icon: 'warning',
    position: 'center',
    showCancelButton: true,
    confirmButtonText: options.confirmButtonText || 'Conferma',
    cancelButtonText: options.cancelButtonText || 'Annulla',
    customClass: {
      popup: 'rounded-2xl',
      confirmButton: 'bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-xl mr-2',
      cancelButton: 'bg-gray-300 hover:bg-gray-400 text-gray-700 font-semibold py-3 px-6 rounded-xl'
    },
    buttonsStyling: false,
    reverseButtons: true
  })
}

export const successAlert = (title: string, text?: string) => {
  return Swal.fire({
    title,
    text,
    icon: 'success',
    position: 'center',
    confirmButtonText: 'OK',
    customClass: {
      popup: 'rounded-2xl',
      confirmButton: 'bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-xl'
    },
    buttonsStyling: false
  })
}

export const errorAlert = (title: string, text?: string) => {
  return Swal.fire({
    title,
    text,
    icon: 'error',
    position: 'center',
    confirmButtonText: 'OK',
    customClass: {
      popup: 'rounded-2xl',
      confirmButton: 'bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-xl'
    },
    buttonsStyling: false
  })
}